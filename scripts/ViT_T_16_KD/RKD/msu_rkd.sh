torchrun --nproc_per_node 1 -m \
    --master_addr=127.0.0.2 --master_port=29455 \
    student.main_kd \
    --t_model ViT-B-16 \
    --model ViT-T-16 \
    --t_model_checkpoint "/home/jiwon/FLIP_T_ckpt/msu_flip_mcl.pth.tar"\
    --config M \
    --op_dir ckpt \
    --report_logger_path log \
    --root "/nas/dataset/FLIP_Dataset/MCIO/frame/"\
    --dataroot "/nas/dataset/FLIP_Dataset/MCIO/txt/"\
    --iterations 15000 \
    --epochs 300 \
    --run 3 \
    --batch_size 8 \
    --total_batch_size 40 \
    --t_batch_size 30 \
    --lr=0.001 \
    --wd=0.1 \
    --alpha_cls_loss 5. \
    --alpha_l2_loss 100. \
    --alpha_ckd_loss 0. \
    --alpha_fd_loss 0. \
    --alpha_affinity_loss 0. \
    --alpha_icl_loss 0.  \
    --dist_ratio  100. \
    --angle_ratio  200. \
    --name "msu(b40,it15000,run3)_rkd_lr0.001"  \
    --swin False \
    --set_wandb True \
    --user jiwon