# e2e
## e2e数据集的命名实体识别


**pytorch ner by bert**


# Requirements

-  `python3`
- `pip3 install -r requirements.txt`


# Run

`python run_ner.py --data_dir=data/ --bert_model=bert-base-cased --task_name=ner --output_dir=out_base --max_seq_length=128 --do_train --num_train_epochs 5 --do_eval --warmup_proportion=0.1`


# Result
             precision    recall  f1-score   support

        FAM     0.9804    0.9910    0.9857       555
       FOOD     0.8792    0.8856    0.8824       682
       NAME     0.8815    0.9005    0.8909       975
       AREA     0.8571    0.9165    0.8858       491
        EAT     0.8065    0.9830    0.8861       530
        PRC     0.8407    0.8617    0.8510       600
       NEAR     0.8288    0.8538    0.8411       465
        RAT     0.8399    0.8648    0.8522       540

avg / total     0.8671    0.9062    0.8855      4838


# PS：
可以将数据集换成你想识别的数据集，只需更改`get_labels`函数
