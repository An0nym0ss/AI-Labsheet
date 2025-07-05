import random
import math

# Dataset with 15 samples and 4 features
data = [
    [2.1, 3.2, 1.8, 2.5],
    [2.3, 3.1, 2.0, 2.4],
    [1.9, 2.8, 1.7, 2.6],
    [2.0, 3.0, 1.9, 2.3],
    [5.2, 6.1, 4.8, 5.5],
    [5.4, 6.3, 5.0, 5.7],
    [5.1, 5.9, 4.9, 5.4],
    [5.3, 6.2, 5.1, 5.6],
    [3.5, 4.2, 3.1, 3.8],
    [3.7, 4.4, 3.3, 4.0],
    [3.4, 4.1, 3.0, 3.7],
    [3.6, 4.3, 3.2, 3.9],
    [1.5, 2.4, 1.3, 1.9],
    [1.7, 2.6, 1.5, 2.1],
    [5.8, 6.7, 5.4, 6.1]
]

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def calculate_centroid(points):
    if not points:
        return [0] * len(data[0])
    n_features = len(points[0])
    centroid = []
    for i in range(n_features):
        centroid.append(sum(point[i] for point in points) / len(points))
    return centroid

def k_means_clustering():
    k = 3
    max_iters = 100
    random.seed(42)
    
    # Initialize centroids randomly from data points
    centroids = random.sample(data, k)
    
    print("Initial centroids:")
    for i, centroid in enumerate(centroids):
        print(f"Centroid {i}: {[f'{x:.3f}' for x in centroid]}")
    
    for iteration in range(max_iters):
        # Assign each point to closest centroid
        cluster_assignments = []
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_cluster = distances.index(min(distances))
            cluster_assignments.append(closest_cluster)
        
        # Calculate new centroids
        new_centroids = []
        for j in range(k):
            cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
            if cluster_points:
                new_centroid = calculate_centroid(cluster_points)
            else:
                new_centroid = centroids[j]
            new_centroids.append(new_centroid)
        
        # Check convergence
        converged = True
        for i in range(k):
            for j in range(len(centroids[i])):
                if abs(centroids[i][j] - new_centroids[i][j]) > 1e-6:
                    converged = False
                    break
            if not converged:
                break
        
        if converged:
            print(f"\nConverged at iteration {iteration + 1}")
            break
        
        centroids = new_centroids
        
        if iteration % 10 == 0:
            print(f"Iteration {iteration + 1}: Centroids updated")
    
    return cluster_assignments, centroids

# Run k-means clustering
cluster_assignments, final_centroids = k_means_clustering()

# Display results
print("\nFinal cluster assignments:")
for idx, cluster in enumerate(cluster_assignments):
    print(f"Sample {idx:2d}: {data[idx]} -> Cluster {cluster}")

print("\nFinal centroid positions:")
for i, centroid in enumerate(final_centroids):
    print(f"Centroid {i}: {[f'{x:.3f}' for x in centroid]}")

# Compute WCSS
wcss = 0
for j in range(3):
    cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
    for point in cluster_points:
        wcss += sum((point[k] - final_centroids[j][k]) ** 2 for k in range(len(point)))

print(f"\nWithin-Cluster Sum of Squares (WCSS): {wcss:.4f}")

# Display cluster summary
print("\nCluster Summary:")
for j in range(3):
    cluster_points = [data[i] for i in range(len(data)) if cluster_assignments[i] == j]
    print(f"Cluster {j}: {len(cluster_points)} points")
    for i, point in enumerate(cluster_points):
        original_idx = data.index(point)
        print(f"  Sample {original_idx}: {[f'{x:.3f}' for x in point]}")

print("\nVisualization (First two features):")
print("Sample | Feature1 | Feature2 | Cluster")
print("-" * 40)
for i in range(len(data)):
    print(f"{i:6d} | {data[i][0]:8.3f} | {data[i][1]:8.3f} | {cluster_assignments[i]:7d}")