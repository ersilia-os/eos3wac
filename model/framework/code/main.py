import os
import sys
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel
from ersilia_pack_utils.core import read_smiles, write_out

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

tokenizer = AutoTokenizer.from_pretrained(checkpoints_dir)
model = AutoModel.from_pretrained(checkpoints_dir)
model.eval()

BATCH_SIZE = 32
N_DIMS = 768
_nan_row = [None] * N_DIMS


def my_model(smiles_list):
    results = []
    for i in range(0, len(smiles_list), BATCH_SIZE):
        batch = smiles_list[i : i + BATCH_SIZE]
        try:
            inputs = tokenizer(
                batch,
                padding="max_length",
                truncation=True,
                max_length=128,
                return_tensors="pt",
            )
            with torch.no_grad():
                out = model(**inputs)
            embeddings = out.last_hidden_state[:, 0, :].numpy()
            for j in range(len(batch)):
                results.append(embeddings[j])
        except Exception:
            results.extend([_nan_row] * len(batch))
    return results


_, smiles_list = read_smiles(input_file)

outputs = my_model(smiles_list)

assert len(smiles_list) == len(outputs)

header = [f"feat_{str(i).zfill(3)}" for i in range(N_DIMS)]

write_out(outputs, header, output_file, np.float32)
