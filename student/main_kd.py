import sys
import json
import numpy as np
import os
import torch
import torch.nn as nn
from datetime import datetime

from teacher.config import configC, configM, configI, configO, config_cefa, config_surf, config_wmca
from teacher.config import config_CI, config_CO , config_CM, config_MC, config_MI, config_MO, config_IC, config_IO, config_IM, config_OC, config_OI, config_OM, custom

from student.params import parse_args
from student.train_flip_mcl_kd import train


torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

device = 'cuda'


def main(args):    
    args = parse_args(args)

    with open(os.path.join(os.getcwd(), 'student/model_config/'+args.t_model+'.json'), 'r') as f:
        args.t_embed_dim = json.load(f)['embed_dim']
    with open(os.path.join(os.getcwd(), 'student/model_config/'+args.model+'.json'), 'r') as f:
        args.s_embed_dim = json.load(f)['embed_dim']

    # get the name of the experiments
    if args.name is None:
        args.name = '-'.join([
            datetime.now().strftime("%Y_%m_%d-%H_%M_%S"),
            f"t_model_{args.t_model}",
            f"s_model_{args.model}",
            f"lr_{args.lr}",
            f"b_{args.batch_size}"
        ])

    # Benchmark 1
    if args.config == 'I':
        config = configI
    if args.config == 'C':
        config = configC
    if args.config == 'M':
        config = configM
    if args.config == 'O':  # 얘 선택할거임
        config = configO

    if args.config == 'custom':
        config = custom

    # Benchmark 2
    if args.config == 'cefa':
        config = config_cefa
    if args.config == 'surf':
        config = config_surf
    if args.config == 'wmca':
        config = config_wmca

    # Benchmark 3
    if args.config == 'CI':
        config = config_CI
    elif args.config == 'CO':
        config = config_CO
    elif args.config == 'CM':
        config = config_CM
    elif args.config == 'MC':
        config = config_MC
    elif args.config == 'MI':
        config = config_MI
    elif args.config == 'MO':
        config = config_MO
    elif args.config == 'IC':
        config = config_IC
    elif args.config == 'IM':
        config = config_IM
    elif args.config == 'IO':
        config = config_IO
    elif args.config == 'OC':
        config = config_OC
    elif args.config == 'OM':
        config = config_OM
    elif args.config == 'OI':
        config = config_OI


    for attr in dir(config):
        if attr.find('__') == -1:
            print('%s = %r' % (attr, getattr(config, attr)))

    config.op_dir = str(args.op_dir)
  
    with open(args.report_logger_path, "w") as f:
        f.write('Run, HTER, AUC, TPR@FPR=1%\n')
        hter_avg = []
        auc_avg = []
        tpr_fpr_avg = []
    
        for i in range(5):
            # To reproduce results
            torch.manual_seed(i)
            np.random.seed(i)

            config.run = i
            config.checkpoint = args.ckpt

            hter, auc, tpr_fpr = train(config, args)

            hter_avg.append(hter)
            auc_avg.append(auc)
            tpr_fpr_avg.append(tpr_fpr)

            f.write(f'{i},{hter},{auc},{tpr_fpr}\n')
    
        hter_mean = np.mean(hter_avg)
        auc_mean = np.mean(auc_avg)
        tpr_fpr_mean = np.mean(tpr_fpr_avg)
        f.write(f'Mean,{hter_mean},{auc_mean},{tpr_fpr_mean}\n')

        hter_std = np.std(hter_avg)
        auc_std = np.std(auc_avg)
        tpr_fpr_std = np.std(tpr_fpr_avg)
        f.write(f'Std dev,{hter_std},{auc_std},{tpr_fpr_std}\n')


if __name__ == "__main__":
    main(sys.argv[1:])