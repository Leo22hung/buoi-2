def exercise1(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
    
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp, fp, and fn must be greater than zero')
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f"Precision is {precision:.4f}")
    print(f"Recall is {recall:.4f}")
    print(f"F1-score is {f1_score:.4f}")

exercise1(tp=2, fp=3, fn=4)
