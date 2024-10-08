torchrun --nproc_per_node 1 -m \
    --master_addr=127.0.0.2 --master_port=29421 \
    plot_tsne \
    --t_model ViT-B-16 \
    --model ViT-T-16 \
    --ckpt "log/vit_msu(b8,it8000)_nodistill_lr0.001/ckpt/flip_mcl_checkpoint_run_4.pth.tar/_checkpoint.pth.tar"\
    --config TSNE \
    --op_dir ckpt \
    --report_logger_path log/tsne.log \
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
    --alpha_fd_loss 0. \
    --alpha_affinity_loss 0.00001 \
    --alpha_icl_loss 0.  \
    --name "tsne"  \
    --swin False