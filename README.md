# Chemistry-Informed Molecular Encoder

Given a SMILES string, returns a fixed-length molecular embedding encoding physicochemical properties and substructure information. Pretrained on 123 million PubChem molecules using a DeBERTaV2 backbone with chemistry-informed objectives beyond masked language modeling. Fine-tunable for property prediction tasks such as solubility, lipophilicity, blood-brain barrier permeability, toxicity, and bioactivity, outperforming SMILES-based encoders on 7 out of 9 MoleculeNet benchmarks.

This model was incorporated on 2026-06-30.Last packaged on 2026-07-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3wac`
- **Slug:** `moldeberta-smiles-encoder`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Chemical language model`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `768`
- **Output Consistency:** `Fixed`
- **Interpretation:** 768-dimensional molecular embedding from a chemistry-informed DeBERTaV2 encoder pretrained on 123M PubChem SMILES.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | MolDeBERTa base model CLS token embedding dimension 0 |
| feat_001 | float |  | MolDeBERTa base model CLS token embedding dimension 1 |
| feat_002 | float |  | MolDeBERTa base model CLS token embedding dimension 2 |
| feat_003 | float |  | MolDeBERTa base model CLS token embedding dimension 3 |
| feat_004 | float |  | MolDeBERTa base model CLS token embedding dimension 4 |
| feat_005 | float |  | MolDeBERTa base model CLS token embedding dimension 5 |
| feat_006 | float |  | MolDeBERTa base model CLS token embedding dimension 6 |
| feat_007 | float |  | MolDeBERTa base model CLS token embedding dimension 7 |
| feat_008 | float |  | MolDeBERTa base model CLS token embedding dimension 8 |
| feat_009 | float |  | MolDeBERTa base model CLS token embedding dimension 9 |

_10 of 768 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3wac](https://hub.docker.com/r/ersiliaos/eos3wac)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3wac.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3wac.zip)

### Resource Consumption
- **Model Size (Mb):** `338`
- **Environment Size (Mb):** `1209`
- **Image Size (Mb):** `1887.02`

**Computational Performance (seconds):**
- 10 inputs: `36.77`
- 100 inputs: `42.52`
- 10000 inputs: `987.93`

### References
- **Source Code**: [https://github.com/pcdslab/MolDeBERTa](https://github.com/pcdslab/MolDeBERTa)
- **Publication**: [https://doi.org/10.64898/2026.02.15.706011](https://doi.org/10.64898/2026.02.15.706011)
- **Publication Type:** `Preprint`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [CC-BY-NC-ND-4.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3wac
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3wac
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
