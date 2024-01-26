# 24accuracy.py by Clarissa Kung

def accuracy(tp, fp, tn, fn):

	if (tp + fp) > 0: precision = tp / (tp + fp)
	else: 		  precision = 0
	
	if (tp + fn) > 0: recall = tp / (tp + fn)
	else: 		  recall = 0
	
	if (precision + recall) > 0: f1_score = 2 * (precision * recall) / (precision + recall)
	else: 			     f1_score = 0
	
	return accuracy, f1_score
	
print(accuracy(80, 10, 120, 5))
print(accuracy(90, 5, 80, 3))
print(accuracy(120, 8, 30, 2))
