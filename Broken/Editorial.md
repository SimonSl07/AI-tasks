**Task Author**: Slănină Simon


### About the Dataset

The dataset contains a mix of AI generated pictures of landscapes, pictures taken by me and pictures taken from the LHQ dataset. It was chosen for this task as I knew it would prove challenging for a model to learn, due to the similarity of tiles containing parts of the sky, of tiles containing trees in a forest etc. .

#### Intended solution

The problem asks us to predict whether pieces of images belong together, and how they are positioned relative to each other. Looking at the data, we can deduce that heuristics like comparing histograms or looking at the similarity of edges will underperform (achieving around 65 - 82 points based on the heuristic chosen). This is because the dataset has been intentionally subjected to **heavy color jittering, random contrast shifts, and Gaussian blurring** that destroys hard edges and lighting consistency.

Because of this, we must rely on Deep Learning to extract high-level features and textures. By using a **pre-trained ResNet18**, we can extract semantic meaning from the tiles and compare them. The overall architecture is best structured as a **Siamese Network**, where both tiles are passed through the same feature extractor, and their resulting embeddings are compared to make a prediction.

First of all, we must build a **synthetic dataset** from the provided training images, as the one provided in the validation data will underperform on subtask 2 (due to a small amount of datapoints). We must make sure to include all pairs of tiles of labels 1, 2, 3 and 4 and supplement them with as many pairs of types 0 and 5 as we can while keeping training time manageable.

For both subtasks we take a pre-trained ResNet18, strip off its final classification layer, and freeze the early layers to save memory and compute. Pass both tile1 and tile2 through this backbone. This gives you two 1D feature vectors.

```py
class PretrainedGlobalCNN(nn.Module):
    def __init__(self, output_dim=256):
        super().__init__()
        resnet = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

        # Strip the final classification layer
        self.backbone = nn.Sequential(*list(resnet.children())[:-1])
        for param in self.backbone.parameters():
            param.requires_grad = False
        for param in self.backbone[7].parameters():
            param.requires_grad = True

        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, output_dim)
        )

    def forward(self, x):
        features = self.backbone(x)
        return self.fc(features)
```

### Subtask 1

To predict wether two tiles are part of the same image, **global embeddings** are of utmost importance. Thus we pass both tiles individually through the encoder, and use the returned embeddings (call them g1 for tile1, g2 for tile2) as well as their difference (g1 - g2) which we send to a shared classifier for both subtasks

### Subtask 2

To predict wether two tiles are neighbours, **edge embeddings** are of utmost importance. Thus, we extract the edges of the images and pass them through a CNN to extract their features. After which, we calculate embeddings of differences between possibly neighbouring edges ( for example, embeddings of right edge of tile1 - embeddings of left edge of tile2) and pass all of them through the shared classifier

#### Model to extract edge embeddings

```py
class EdgeCNN(nn.Module):
    def __init__(self, output_dim=128):
        super().__init__()
        # Input shape: (Batch, 3, 16, 128)

        #Squash edge to 1D 
        self.squash_conv = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=(16, 3), padding=(0, 1)),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )

        self.seq_conv = nn.Sequential(
            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(2),

            nn.Conv1d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(16) # Compress to 16 key features
        )

        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 16, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, output_dim)
        )

    def forward(self, x):
        x = self.squash_conv(x)      # (B, 64, 1, 128)
        x = x.squeeze(2)             # Remove the 1 -> (B, 64, 128)
        x = self.seq_conv(x)         # (B, 128, 16)
        return self.fc(x)
```

### Final model

```py
class RelationalBrokenTileNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.global_net = PretrainedGlobalCNN(output_dim=256)
        self.edge_net = EdgeCNN(output_dim=128)

        self.classifier = nn.Sequential(
            nn.Linear(1280, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.25),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.2),
            nn.Linear(256, 6)
        )

    def extract_edges(self, img):
        top, bottom = img[:, :, :16, :], img[:, :, -16:, :]
        left, right = img[:, :, :, :16].transpose(2, 3), img[:, :, :, -16:].transpose(2, 3)
        return top, bottom, left, right

    def forward(self, img1, img2):
        g1, g2 = self.global_net(img1), self.global_net(img2)
        t1, b1, l1, r1 = self.extract_edges(img1)
        t2, b2, l2, r2 = self.extract_edges(img2)

        e1_t, e1_b, e1_l, e1_r = self.edge_net(t1), self.edge_net(b1), self.edge_net(l1), self.edge_net(r1)
        e2_t, e2_b, e2_l, e2_r = self.edge_net(t2), self.edge_net(b2), self.edge_net(l2), self.edge_net(r2)

        g_diff = torch.abs(g1 - g2)

        lr_diff = torch.abs(e1_r - e2_l)
        ab_diff = torch.abs(e1_b - e2_t)
        rl_diff = torch.abs(e1_l - e2_r)
        ba_diff = torch.abs(e1_t - e2_b)

        features = torch.cat([
            g1, g2, g_diff,
            lr_diff, ab_diff, rl_diff, ba_diff
        ], dim=1)

        return self.classifier(features)

```

Due to the inherent imbalance of the dataset, computing **class weights** for the loss function is a must!

