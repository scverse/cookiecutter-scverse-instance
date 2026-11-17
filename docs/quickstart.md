# Quickstart

cookiecutter-scverse-instance works on {class}`~anndata.AnnData` objects: {mod}`cookiecutter_scverse_instance.pp` preprocesses them, {mod}`cookiecutter_scverse_instance.tl` computes on them and {mod}`cookiecutter_scverse_instance.pl` plots them.

```python
import numpy as np
from anndata import AnnData

import cookiecutter_scverse_instance

adata = AnnData(np.random.normal(size=(20, 10)))

cookiecutter_scverse_instance.pp.basic_preproc(adata)
cookiecutter_scverse_instance.tl.basic_tool(adata)
cookiecutter_scverse_instance.pl.basic_plot(adata)
```

The {doc}`tutorials <notebooks/example>` go into more detail and the {doc}`API reference <api>` lists every function.
