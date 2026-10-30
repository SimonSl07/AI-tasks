baseline = 0
best_score = 0.87

def score(metric):
  if metric < baseline:
    return 4
  if metric <= best_score:
    return 4 + int((metric - baseline) * 36 / (best_score - baseline))
  return 40

submission['correct_values'] = submission['correct_values'].astype(float).astype(int)
submission['output_values'] = submission['output_values'].astype(float).astype(int)

partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = metrics.matthews_corrcoef(partial['correct_values'], partial['output_values'])
partial_score = score(partial_metric)

complete_metric = metrics.matthews_corrcoef(submission['correct_values'], submission['output_values'])
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric