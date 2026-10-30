aseline = 0.26
best_score = 0.8

def score(metric):
  if metric < baseline:
    return 6
  if metric <= best_score:
    return 6 + int((metric - baseline) * 54 / (best_score - baseline))
  return 60

def perspective_metric(y_true, y_pred):
        y_true = pd.to_numeric(y_true, errors='coerce')
        y_pred = pd.to_numeric(y_pred, errors='coerce')
        diff = np.abs(y_true - y_pred)
        z = np.minimum(diff, 360 - diff)
        item_scores = np.maximum(0, 1 - z / 90)
        return np.mean(item_scores) # Returns average accuracy percentage (0.0 to 1.0)

partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = perspective_metric(partial['correct_values'], partial['output_values'])
partial_score = score(partial_metric)

complete_metric = perspective_metric(submission['correct_values'], submission['output_values'])
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric