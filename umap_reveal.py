import pandas as pd
import bpy
C = bpy.context

def umap_reveal(df = pd.DataFrame):
    for i in range(len(df)):
        x,y,z = df.iloc[i][[1,2,3]]
        bpy.ops.mesh.primitive_cube_add(size = .1, location = (x,y,z))
        item = C.object
        item.data.materials.append(bpy.data.materials[str(df.iloc[i]["seurat_clusters"])]) # appends a material according to the cluster of the cell

df = pd.read_table("UMAP_coord.tsv", sep="\t")
umap_reveal(df)