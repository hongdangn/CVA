from .proposal_loss_with_DTW import ProposalLossWithDTW

criterion_list = {
    "ours": ProposalLossWithDTW,
}

def build_criterion(args):
    if args.kd_loss_type not in criterion_list.keys():
        raise ValueError(f"Criterion {args.kd_loss_type} not found.")
    return criterion_list[args.kd_loss_type](args)