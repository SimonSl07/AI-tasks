baseline = 0.261
best_score = 0.67

def score(metric):
  if metric <= baseline:
     return 4
  if metric <= best_score:
    ans = (metric - baseline) / (best_score - baseline)
    ans = (np.exp(3 * ans) - 1) / (np.exp(3) - 1)
    return min(int(ans * 36.0) + 4, 40)
  return 40
partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = metrics.f1_score(partial['correct_values'] == "0", partial['output_values'] == "0", average="macro", pos_label=True)
partial_score = score(partial_metric)

complete_metric = metrics.f1_score(submission['correct_values'] == "0", submission['output_values'] == "0", average="macro", pos_label=True)
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric