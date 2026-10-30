baseline = 0
best_score = 0.53

def score(metric):
  if metric < baseline:
    return 6
  if metric <= best_score:
    return 6 + int((metric - baseline) * 54 / (best_score - baseline))
  return 60


submission['correct_values'] = submission['correct_values'].astype(float).astype(int)
submission['output_values'] = submission['output_values'].astype(float).astype(int)
partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = metrics.adjusted_mutual_info_score(partial['correct_values'], partial['output_values'])
partial_score = score(partial_metric)

complete_metric = metrics.adjusted_mutual_info_score(submission['correct_values'], submission['output_values'])
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric