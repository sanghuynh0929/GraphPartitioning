import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def solve(affinity, n, m, k, epsilon, time):
    W = np.array(affinity)
    D = [[np.sum(W, axis=0)[i] if i == j else 0 for i in range (n)]
         for j in range (n)]
    L = np.array(D-W)
    eigenvals, eigenvcts = np.linalg.eig(L)
    def project_and_transpose(eigenvals, eigenvcts, num_ev):
        """Select the eigenvectors corresponding to the first
        (sorted) num_ev eigenvalues as columns in a data frame.
        """
        eigenvals_sorted_indices = np.argsort(eigenvals)
        indices = eigenvals_sorted_indices[: num_ev]

        proj_df = pd.DataFrame(eigenvcts[:, indices.squeeze()])
        proj_df.columns = ['v_' + str(c) for c in proj_df.columns]
        return proj_df

    proj_df = project_and_transpose(eigenvals, eigenvcts, num_ev=k)

    def run_k_means(df, n_clusters):
        """K-means clustering."""
        k_means = KMeans(random_state=25, n_clusters=n_clusters)
        k_means.fit(df)
        cluster = k_means.predict(df)
        return cluster

    cluster = run_k_means(proj_df, n_clusters=k)
    return cluster
