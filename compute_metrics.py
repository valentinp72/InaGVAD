#/!usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--prediction_dir', required=True)
parser.add_argument('--num_boots', type=int, default=1000)
parser.add_argument('--type', default='global', choices=['global', 'channel_type'])
args = parser.parse_args()

from inaGVAD.vad_metrics import VadEval
dref = '/mnt/rex/home17/vpelloin/git/InaGVAD_bootstrap/'
vad = VadEval(num_boots=args.num_boots)
results = vad.evaluation(dref, args.prediction_dir, 'test', args.type)

import pickle
with open(f'{args.prediction_dir}/{args.type}.pickle', 'wb') as f:
    pickle.dump(results, file=f)
