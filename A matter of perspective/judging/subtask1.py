baseline = 0.33
best_score = .8

def score(metric):
  if metric < baseline:
    return 4
  if metric <= best_score:
    return 4 + int((metric - baseline) * 36 / (best_score - baseline))
  return 40

partial, rest = model_selection.train_test_split(submission, test_size=0.3, random_state=0)

partial_metric = metrics.accuracy_score(partial['correct_values'], partial['output_values'])
partial_score = score(partial_metric)

complete_metric = metrics.accuracy_score(submission['correct_values'], submission['output_values'])
complete_score = score(complete_metric)

return partial_score, partial_metric, complete_score, complete_metric