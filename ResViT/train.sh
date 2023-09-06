python convout64.py --classname="normal" --path="train/normal/"
python convout64.py --classname="severe" --path="train/severe/"

python train.py --num_classes=2 --epochs=50 --batch-size=128 --pick=123 --data-path="train"
