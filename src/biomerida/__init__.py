__version__ = "0.0.1"

from .data import add_templated_examples, get_templated_dataset, sample_dataset
from .modeling import BitFitHead, BitFitModel
from .trainer import BitFitTrainer
# from .trainer_distillation import DistillationSetFitTrainer
