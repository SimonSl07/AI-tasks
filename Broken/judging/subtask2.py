baseline = 0.087
best_score = 0.36

def score(metric):
  if metric <= baseline:
     return 6
  if metric <= best_score:
    ans = (metric - baseline) / (best_score - baseline)
    ans = (np.exp(3 * ans) - 1) / (np.exp(3) - 1)
    return min(int(ans * 54.0) + 6, 60)
  return 60

partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = metrics.f1_score(partial['correct_values'], partial['output_values'], average="macro", pos_label="true")
partial_score = score(partial_metric)

complete_metric = metrics.f1_score(submission['correct_values'], submission['output_values'], average="macro", pos_label="true")
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric