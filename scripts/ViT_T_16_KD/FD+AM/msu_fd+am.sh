torchrun --nproc_per_node 1 -m \
    --master_addr=127.0.0.2 --master_port=29491 \
    train.main_kd \
    --t_model ViT-B-16 \
    --model ViT-T-16 \
    --t_model_checkpoint "/home/jiwon/FLIP_T_ckpt/msu_flip_mcl.pth.tar"\
    --config M \
    --op_dir ckpt \
    --report_logger_path log \
    --root "/nas/dataset/FLIP_Dataset/MCIO/frame/"\
    --dataroot "/nas/dataset/FLIP_Dataset/MCIO/txt/"\
    --iterations 4000 \
    --epochs 300 \
    --batch_size 8 \
    --total_batch_size 8 \
    --t_batch_size 30 \
    --lr=0.001 \
    --wd=0.1 \
    --alpha_ckd_loss 0. \
    --alpha_fd_loss 10. \
    --alpha_affinity_loss 0.00001 \
    --alpha_icl_loss 0.  \
    --name "msu(b8,it4000)_fd10+am0.00001_lr0.001"  \
    --swin False \
    --set_wandb True \
    --user jiwon