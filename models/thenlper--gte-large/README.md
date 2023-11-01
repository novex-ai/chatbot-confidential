---
tags:
- mteb
- sentence-similarity
- sentence-transformers
- Sentence Transformers
model-index:
- name: gte-large
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 72.62686567164178
    - type: ap
      value: 34.46944126809772
    - type: f1
      value: 66.23684353950857
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 92.51805
    - type: ap
      value: 89.49842783330848
    - type: f1
      value: 92.51112169431808
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 49.074
    - type: f1
      value: 48.44785682572955
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.077
    - type: map_at_10
      value: 48.153
    - type: map_at_100
      value: 48.963
    - type: map_at_1000
      value: 48.966
    - type: map_at_3
      value: 43.184
    - type: map_at_5
      value: 46.072
    - type: mrr_at_1
      value: 33.073
    - type: mrr_at_10
      value: 48.54
    - type: mrr_at_100
      value: 49.335
    - type: mrr_at_1000
      value: 49.338
    - type: mrr_at_3
      value: 43.563
    - type: mrr_at_5
      value: 46.383
    - type: ndcg_at_1
      value: 32.077
    - type: ndcg_at_10
      value: 57.158
    - type: ndcg_at_100
      value: 60.324999999999996
    - type: ndcg_at_1000
      value: 60.402
    - type: ndcg_at_3
      value: 46.934
    - type: ndcg_at_5
      value: 52.158
    - type: precision_at_1
      value: 32.077
    - type: precision_at_10
      value: 8.591999999999999
    - type: precision_at_100
      value: 0.991
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 19.275000000000002
    - type: precision_at_5
      value: 14.111
    - type: recall_at_1
      value: 32.077
    - type: recall_at_10
      value: 85.917
    - type: recall_at_100
      value: 99.075
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_3
      value: 57.824
    - type: recall_at_5
      value: 70.555
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 48.619246083417295
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 43.3574067664688
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 63.06359661829253
    - type: mrr
      value: 76.15596007562766
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 90.25407547368691
    - type: cos_sim_spearman
      value: 88.65081514968477
    - type: euclidean_pearson
      value: 88.14857116664494
    - type: euclidean_spearman
      value: 88.50683596540692
    - type: manhattan_pearson
      value: 87.9654797992225
    - type: manhattan_spearman
      value: 88.21164851646908
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 86.05844155844157
    - type: f1
      value: 86.01555597681825
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 39.10510519739522
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 36.84689960264385
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.800000000000004
    - type: map_at_10
      value: 44.857
    - type: map_at_100
      value: 46.512
    - type: map_at_1000
      value: 46.635
    - type: map_at_3
      value: 41.062
    - type: map_at_5
      value: 43.126
    - type: mrr_at_1
      value: 39.628
    - type: mrr_at_10
      value: 50.879
    - type: mrr_at_100
      value: 51.605000000000004
    - type: mrr_at_1000
      value: 51.641000000000005
    - type: mrr_at_3
      value: 48.14
    - type: mrr_at_5
      value: 49.835
    - type: ndcg_at_1
      value: 39.628
    - type: ndcg_at_10
      value: 51.819
    - type: ndcg_at_100
      value: 57.318999999999996
    - type: ndcg_at_1000
      value: 58.955999999999996
    - type: ndcg_at_3
      value: 46.409
    - type: ndcg_at_5
      value: 48.825
    - type: precision_at_1
      value: 39.628
    - type: precision_at_10
      value: 10.072000000000001
    - type: precision_at_100
      value: 1.625
    - type: precision_at_1000
      value: 0.21
    - type: precision_at_3
      value: 22.556
    - type: precision_at_5
      value: 16.309
    - type: recall_at_1
      value: 32.800000000000004
    - type: recall_at_10
      value: 65.078
    - type: recall_at_100
      value: 87.491
    - type: recall_at_1000
      value: 97.514
    - type: recall_at_3
      value: 49.561
    - type: recall_at_5
      value: 56.135999999999996
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.614
    - type: map_at_10
      value: 43.578
    - type: map_at_100
      value: 44.897
    - type: map_at_1000
      value: 45.023
    - type: map_at_3
      value: 40.282000000000004
    - type: map_at_5
      value: 42.117
    - type: mrr_at_1
      value: 40.510000000000005
    - type: mrr_at_10
      value: 49.428
    - type: mrr_at_100
      value: 50.068999999999996
    - type: mrr_at_1000
      value: 50.111000000000004
    - type: mrr_at_3
      value: 47.176
    - type: mrr_at_5
      value: 48.583999999999996
    - type: ndcg_at_1
      value: 40.510000000000005
    - type: ndcg_at_10
      value: 49.478
    - type: ndcg_at_100
      value: 53.852
    - type: ndcg_at_1000
      value: 55.782
    - type: ndcg_at_3
      value: 45.091
    - type: ndcg_at_5
      value: 47.19
    - type: precision_at_1
      value: 40.510000000000005
    - type: precision_at_10
      value: 9.363000000000001
    - type: precision_at_100
      value: 1.51
    - type: precision_at_1000
      value: 0.196
    - type: precision_at_3
      value: 21.741
    - type: precision_at_5
      value: 15.465000000000002
    - type: recall_at_1
      value: 32.614
    - type: recall_at_10
      value: 59.782000000000004
    - type: recall_at_100
      value: 78.012
    - type: recall_at_1000
      value: 90.319
    - type: recall_at_3
      value: 46.825
    - type: recall_at_5
      value: 52.688
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 40.266000000000005
    - type: map_at_10
      value: 53.756
    - type: map_at_100
      value: 54.809
    - type: map_at_1000
      value: 54.855
    - type: map_at_3
      value: 50.073
    - type: map_at_5
      value: 52.293
    - type: mrr_at_1
      value: 46.332
    - type: mrr_at_10
      value: 57.116
    - type: mrr_at_100
      value: 57.767
    - type: mrr_at_1000
      value: 57.791000000000004
    - type: mrr_at_3
      value: 54.461999999999996
    - type: mrr_at_5
      value: 56.092
    - type: ndcg_at_1
      value: 46.332
    - type: ndcg_at_10
      value: 60.092
    - type: ndcg_at_100
      value: 64.034
    - type: ndcg_at_1000
      value: 64.937
    - type: ndcg_at_3
      value: 54.071000000000005
    - type: ndcg_at_5
      value: 57.254000000000005
    - type: precision_at_1
      value: 46.332
    - type: precision_at_10
      value: 9.799
    - type: precision_at_100
      value: 1.278
    - type: precision_at_1000
      value: 0.13899999999999998
    - type: precision_at_3
      value: 24.368000000000002
    - type: precision_at_5
      value: 16.89
    - type: recall_at_1
      value: 40.266000000000005
    - type: recall_at_10
      value: 75.41499999999999
    - type: recall_at_100
      value: 92.01700000000001
    - type: recall_at_1000
      value: 98.379
    - type: recall_at_3
      value: 59.476
    - type: recall_at_5
      value: 67.297
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 28.589
    - type: map_at_10
      value: 37.755
    - type: map_at_100
      value: 38.881
    - type: map_at_1000
      value: 38.954
    - type: map_at_3
      value: 34.759
    - type: map_at_5
      value: 36.544
    - type: mrr_at_1
      value: 30.734
    - type: mrr_at_10
      value: 39.742
    - type: mrr_at_100
      value: 40.774
    - type: mrr_at_1000
      value: 40.824
    - type: mrr_at_3
      value: 37.137
    - type: mrr_at_5
      value: 38.719
    - type: ndcg_at_1
      value: 30.734
    - type: ndcg_at_10
      value: 42.978
    - type: ndcg_at_100
      value: 48.309000000000005
    - type: ndcg_at_1000
      value: 50.068
    - type: ndcg_at_3
      value: 37.361
    - type: ndcg_at_5
      value: 40.268
    - type: precision_at_1
      value: 30.734
    - type: precision_at_10
      value: 6.565
    - type: precision_at_100
      value: 0.964
    - type: precision_at_1000
      value: 0.11499999999999999
    - type: precision_at_3
      value: 15.744
    - type: precision_at_5
      value: 11.096
    - type: recall_at_1
      value: 28.589
    - type: recall_at_10
      value: 57.126999999999995
    - type: recall_at_100
      value: 81.051
    - type: recall_at_1000
      value: 94.027
    - type: recall_at_3
      value: 42.045
    - type: recall_at_5
      value: 49.019
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 18.5
    - type: map_at_10
      value: 27.950999999999997
    - type: map_at_100
      value: 29.186
    - type: map_at_1000
      value: 29.298000000000002
    - type: map_at_3
      value: 25.141000000000002
    - type: map_at_5
      value: 26.848
    - type: mrr_at_1
      value: 22.637
    - type: mrr_at_10
      value: 32.572
    - type: mrr_at_100
      value: 33.472
    - type: mrr_at_1000
      value: 33.533
    - type: mrr_at_3
      value: 29.747
    - type: mrr_at_5
      value: 31.482
    - type: ndcg_at_1
      value: 22.637
    - type: ndcg_at_10
      value: 33.73
    - type: ndcg_at_100
      value: 39.568
    - type: ndcg_at_1000
      value: 42.201
    - type: ndcg_at_3
      value: 28.505999999999997
    - type: ndcg_at_5
      value: 31.255
    - type: precision_at_1
      value: 22.637
    - type: precision_at_10
      value: 6.281000000000001
    - type: precision_at_100
      value: 1.073
    - type: precision_at_1000
      value: 0.14300000000000002
    - type: precision_at_3
      value: 13.847000000000001
    - type: precision_at_5
      value: 10.224
    - type: recall_at_1
      value: 18.5
    - type: recall_at_10
      value: 46.744
    - type: recall_at_100
      value: 72.072
    - type: recall_at_1000
      value: 91.03999999999999
    - type: recall_at_3
      value: 32.551
    - type: recall_at_5
      value: 39.533
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.602
    - type: map_at_10
      value: 42.18
    - type: map_at_100
      value: 43.6
    - type: map_at_1000
      value: 43.704
    - type: map_at_3
      value: 38.413000000000004
    - type: map_at_5
      value: 40.626
    - type: mrr_at_1
      value: 37.344
    - type: mrr_at_10
      value: 47.638000000000005
    - type: mrr_at_100
      value: 48.485
    - type: mrr_at_1000
      value: 48.52
    - type: mrr_at_3
      value: 44.867000000000004
    - type: mrr_at_5
      value: 46.566
    - type: ndcg_at_1
      value: 37.344
    - type: ndcg_at_10
      value: 48.632
    - type: ndcg_at_100
      value: 54.215
    - type: ndcg_at_1000
      value: 55.981
    - type: ndcg_at_3
      value: 42.681999999999995
    - type: ndcg_at_5
      value: 45.732
    - type: precision_at_1
      value: 37.344
    - type: precision_at_10
      value: 8.932
    - type: precision_at_100
      value: 1.376
    - type: precision_at_1000
      value: 0.17099999999999999
    - type: precision_at_3
      value: 20.276
    - type: precision_at_5
      value: 14.726
    - type: recall_at_1
      value: 30.602
    - type: recall_at_10
      value: 62.273
    - type: recall_at_100
      value: 85.12100000000001
    - type: recall_at_1000
      value: 96.439
    - type: recall_at_3
      value: 45.848
    - type: recall_at_5
      value: 53.615
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 23.952
    - type: map_at_10
      value: 35.177
    - type: map_at_100
      value: 36.59
    - type: map_at_1000
      value: 36.703
    - type: map_at_3
      value: 31.261
    - type: map_at_5
      value: 33.222
    - type: mrr_at_1
      value: 29.337999999999997
    - type: mrr_at_10
      value: 40.152
    - type: mrr_at_100
      value: 40.963
    - type: mrr_at_1000
      value: 41.016999999999996
    - type: mrr_at_3
      value: 36.91
    - type: mrr_at_5
      value: 38.685
    - type: ndcg_at_1
      value: 29.337999999999997
    - type: ndcg_at_10
      value: 41.994
    - type: ndcg_at_100
      value: 47.587
    - type: ndcg_at_1000
      value: 49.791000000000004
    - type: ndcg_at_3
      value: 35.27
    - type: ndcg_at_5
      value: 38.042
    - type: precision_at_1
      value: 29.337999999999997
    - type: precision_at_10
      value: 8.276
    - type: precision_at_100
      value: 1.276
    - type: precision_at_1000
      value: 0.164
    - type: precision_at_3
      value: 17.161
    - type: precision_at_5
      value: 12.671
    - type: recall_at_1
      value: 23.952
    - type: recall_at_10
      value: 57.267
    - type: recall_at_100
      value: 80.886
    - type: recall_at_1000
      value: 95.611
    - type: recall_at_3
      value: 38.622
    - type: recall_at_5
      value: 45.811
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.092083333333335
    - type: map_at_10
      value: 37.2925
    - type: map_at_100
      value: 38.57041666666666
    - type: map_at_1000
      value: 38.68141666666667
    - type: map_at_3
      value: 34.080000000000005
    - type: map_at_5
      value: 35.89958333333333
    - type: mrr_at_1
      value: 31.94758333333333
    - type: mrr_at_10
      value: 41.51049999999999
    - type: mrr_at_100
      value: 42.36099999999999
    - type: mrr_at_1000
      value: 42.4125
    - type: mrr_at_3
      value: 38.849583333333335
    - type: mrr_at_5
      value: 40.448249999999994
    - type: ndcg_at_1
      value: 31.94758333333333
    - type: ndcg_at_10
      value: 43.17633333333333
    - type: ndcg_at_100
      value: 48.45241666666668
    - type: ndcg_at_1000
      value: 50.513999999999996
    - type: ndcg_at_3
      value: 37.75216666666667
    - type: ndcg_at_5
      value: 40.393833333333326
    - type: precision_at_1
      value: 31.94758333333333
    - type: precision_at_10
      value: 7.688916666666666
    - type: precision_at_100
      value: 1.2250833333333333
    - type: precision_at_1000
      value: 0.1595
    - type: precision_at_3
      value: 17.465999999999998
    - type: precision_at_5
      value: 12.548083333333333
    - type: recall_at_1
      value: 27.092083333333335
    - type: recall_at_10
      value: 56.286583333333326
    - type: recall_at_100
      value: 79.09033333333333
    - type: recall_at_1000
      value: 93.27483333333335
    - type: recall_at_3
      value: 41.35325
    - type: recall_at_5
      value: 48.072750000000006
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.825
    - type: map_at_10
      value: 33.723
    - type: map_at_100
      value: 34.74
    - type: map_at_1000
      value: 34.824
    - type: map_at_3
      value: 31.369000000000003
    - type: map_at_5
      value: 32.533
    - type: mrr_at_1
      value: 29.293999999999997
    - type: mrr_at_10
      value: 36.84
    - type: mrr_at_100
      value: 37.681
    - type: mrr_at_1000
      value: 37.742
    - type: mrr_at_3
      value: 34.79
    - type: mrr_at_5
      value: 35.872
    - type: ndcg_at_1
      value: 29.293999999999997
    - type: ndcg_at_10
      value: 38.385999999999996
    - type: ndcg_at_100
      value: 43.327
    - type: ndcg_at_1000
      value: 45.53
    - type: ndcg_at_3
      value: 33.985
    - type: ndcg_at_5
      value: 35.817
    - type: precision_at_1
      value: 29.293999999999997
    - type: precision_at_10
      value: 6.12
    - type: precision_at_100
      value: 0.9329999999999999
    - type: precision_at_1000
      value: 0.11900000000000001
    - type: precision_at_3
      value: 14.621999999999998
    - type: precision_at_5
      value: 10.030999999999999
    - type: recall_at_1
      value: 25.825
    - type: recall_at_10
      value: 49.647000000000006
    - type: recall_at_100
      value: 72.32300000000001
    - type: recall_at_1000
      value: 88.62400000000001
    - type: recall_at_3
      value: 37.366
    - type: recall_at_5
      value: 41.957
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 18.139
    - type: map_at_10
      value: 26.107000000000003
    - type: map_at_100
      value: 27.406999999999996
    - type: map_at_1000
      value: 27.535999999999998
    - type: map_at_3
      value: 23.445
    - type: map_at_5
      value: 24.916
    - type: mrr_at_1
      value: 21.817
    - type: mrr_at_10
      value: 29.99
    - type: mrr_at_100
      value: 31.052000000000003
    - type: mrr_at_1000
      value: 31.128
    - type: mrr_at_3
      value: 27.627000000000002
    - type: mrr_at_5
      value: 29.005
    - type: ndcg_at_1
      value: 21.817
    - type: ndcg_at_10
      value: 31.135
    - type: ndcg_at_100
      value: 37.108000000000004
    - type: ndcg_at_1000
      value: 39.965
    - type: ndcg_at_3
      value: 26.439
    - type: ndcg_at_5
      value: 28.655
    - type: precision_at_1
      value: 21.817
    - type: precision_at_10
      value: 5.757000000000001
    - type: precision_at_100
      value: 1.036
    - type: precision_at_1000
      value: 0.147
    - type: precision_at_3
      value: 12.537
    - type: precision_at_5
      value: 9.229
    - type: recall_at_1
      value: 18.139
    - type: recall_at_10
      value: 42.272999999999996
    - type: recall_at_100
      value: 68.657
    - type: recall_at_1000
      value: 88.93799999999999
    - type: recall_at_3
      value: 29.266
    - type: recall_at_5
      value: 34.892
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.755000000000003
    - type: map_at_10
      value: 37.384
    - type: map_at_100
      value: 38.56
    - type: map_at_1000
      value: 38.655
    - type: map_at_3
      value: 34.214
    - type: map_at_5
      value: 35.96
    - type: mrr_at_1
      value: 32.369
    - type: mrr_at_10
      value: 41.625
    - type: mrr_at_100
      value: 42.449
    - type: mrr_at_1000
      value: 42.502
    - type: mrr_at_3
      value: 38.899
    - type: mrr_at_5
      value: 40.489999999999995
    - type: ndcg_at_1
      value: 32.369
    - type: ndcg_at_10
      value: 43.287
    - type: ndcg_at_100
      value: 48.504999999999995
    - type: ndcg_at_1000
      value: 50.552
    - type: ndcg_at_3
      value: 37.549
    - type: ndcg_at_5
      value: 40.204
    - type: precision_at_1
      value: 32.369
    - type: precision_at_10
      value: 7.425
    - type: precision_at_100
      value: 1.134
    - type: precision_at_1000
      value: 0.14200000000000002
    - type: precision_at_3
      value: 17.102
    - type: precision_at_5
      value: 12.107999999999999
    - type: recall_at_1
      value: 27.755000000000003
    - type: recall_at_10
      value: 57.071000000000005
    - type: recall_at_100
      value: 79.456
    - type: recall_at_1000
      value: 93.54299999999999
    - type: recall_at_3
      value: 41.298
    - type: recall_at_5
      value: 48.037
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.855
    - type: map_at_10
      value: 34.53
    - type: map_at_100
      value: 36.167
    - type: map_at_1000
      value: 36.394999999999996
    - type: map_at_3
      value: 31.037
    - type: map_at_5
      value: 33.119
    - type: mrr_at_1
      value: 30.631999999999998
    - type: mrr_at_10
      value: 39.763999999999996
    - type: mrr_at_100
      value: 40.77
    - type: mrr_at_1000
      value: 40.826
    - type: mrr_at_3
      value: 36.495
    - type: mrr_at_5
      value: 38.561
    - type: ndcg_at_1
      value: 30.631999999999998
    - type: ndcg_at_10
      value: 40.942
    - type: ndcg_at_100
      value: 47.07
    - type: ndcg_at_1000
      value: 49.363
    - type: ndcg_at_3
      value: 35.038000000000004
    - type: ndcg_at_5
      value: 38.161
    - type: precision_at_1
      value: 30.631999999999998
    - type: precision_at_10
      value: 7.983999999999999
    - type: precision_at_100
      value: 1.6070000000000002
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_3
      value: 16.206
    - type: precision_at_5
      value: 12.253
    - type: recall_at_1
      value: 24.855
    - type: recall_at_10
      value: 53.291999999999994
    - type: recall_at_100
      value: 80.283
    - type: recall_at_1000
      value: 94.309
    - type: recall_at_3
      value: 37.257
    - type: recall_at_5
      value: 45.282
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 21.208
    - type: map_at_10
      value: 30.512
    - type: map_at_100
      value: 31.496000000000002
    - type: map_at_1000
      value: 31.595000000000002
    - type: map_at_3
      value: 27.904
    - type: map_at_5
      value: 29.491
    - type: mrr_at_1
      value: 22.736
    - type: mrr_at_10
      value: 32.379999999999995
    - type: mrr_at_100
      value: 33.245000000000005
    - type: mrr_at_1000
      value: 33.315
    - type: mrr_at_3
      value: 29.945
    - type: mrr_at_5
      value: 31.488
    - type: ndcg_at_1
      value: 22.736
    - type: ndcg_at_10
      value: 35.643
    - type: ndcg_at_100
      value: 40.535
    - type: ndcg_at_1000
      value: 43.042
    - type: ndcg_at_3
      value: 30.625000000000004
    - type: ndcg_at_5
      value: 33.323
    - type: precision_at_1
      value: 22.736
    - type: precision_at_10
      value: 5.6930000000000005
    - type: precision_at_100
      value: 0.889
    - type: precision_at_1000
      value: 0.122
    - type: precision_at_3
      value: 13.431999999999999
    - type: precision_at_5
      value: 9.575
    - type: recall_at_1
      value: 21.208
    - type: recall_at_10
      value: 49.47
    - type: recall_at_100
      value: 71.71499999999999
    - type: recall_at_1000
      value: 90.55499999999999
    - type: recall_at_3
      value: 36.124
    - type: recall_at_5
      value: 42.606
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 11.363
    - type: map_at_10
      value: 20.312
    - type: map_at_100
      value: 22.225
    - type: map_at_1000
      value: 22.411
    - type: map_at_3
      value: 16.68
    - type: map_at_5
      value: 18.608
    - type: mrr_at_1
      value: 25.537
    - type: mrr_at_10
      value: 37.933
    - type: mrr_at_100
      value: 38.875
    - type: mrr_at_1000
      value: 38.911
    - type: mrr_at_3
      value: 34.387
    - type: mrr_at_5
      value: 36.51
    - type: ndcg_at_1
      value: 25.537
    - type: ndcg_at_10
      value: 28.82
    - type: ndcg_at_100
      value: 36.341
    - type: ndcg_at_1000
      value: 39.615
    - type: ndcg_at_3
      value: 23.01
    - type: ndcg_at_5
      value: 25.269000000000002
    - type: precision_at_1
      value: 25.537
    - type: precision_at_10
      value: 9.153
    - type: precision_at_100
      value: 1.7319999999999998
    - type: precision_at_1000
      value: 0.234
    - type: precision_at_3
      value: 17.22
    - type: precision_at_5
      value: 13.629
    - type: recall_at_1
      value: 11.363
    - type: recall_at_10
      value: 35.382999999999996
    - type: recall_at_100
      value: 61.367000000000004
    - type: recall_at_1000
      value: 79.699
    - type: recall_at_3
      value: 21.495
    - type: recall_at_5
      value: 27.42
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 9.65
    - type: map_at_10
      value: 20.742
    - type: map_at_100
      value: 29.614
    - type: map_at_1000
      value: 31.373
    - type: map_at_3
      value: 14.667
    - type: map_at_5
      value: 17.186
    - type: mrr_at_1
      value: 69.75
    - type: mrr_at_10
      value: 76.762
    - type: mrr_at_100
      value: 77.171
    - type: mrr_at_1000
      value: 77.179
    - type: mrr_at_3
      value: 75.125
    - type: mrr_at_5
      value: 76.287
    - type: ndcg_at_1
      value: 57.62500000000001
    - type: ndcg_at_10
      value: 42.370999999999995
    - type: ndcg_at_100
      value: 47.897
    - type: ndcg_at_1000
      value: 55.393
    - type: ndcg_at_3
      value: 46.317
    - type: ndcg_at_5
      value: 43.906
    - type: precision_at_1
      value: 69.75
    - type: precision_at_10
      value: 33.95
    - type: precision_at_100
      value: 10.885
    - type: precision_at_1000
      value: 2.2239999999999998
    - type: precision_at_3
      value: 49.75
    - type: precision_at_5
      value: 42.3
    - type: recall_at_1
      value: 9.65
    - type: recall_at_10
      value: 26.117
    - type: recall_at_100
      value: 55.084
    - type: recall_at_1000
      value: 78.62400000000001
    - type: recall_at_3
      value: 15.823
    - type: recall_at_5
      value: 19.652
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 47.885
    - type: f1
      value: 42.99567641346983
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.97
    - type: map_at_10
      value: 80.34599999999999
    - type: map_at_100
      value: 80.571
    - type: map_at_1000
      value: 80.584
    - type: map_at_3
      value: 79.279
    - type: map_at_5
      value: 79.94
    - type: mrr_at_1
      value: 76.613
    - type: mrr_at_10
      value: 85.15700000000001
    - type: mrr_at_100
      value: 85.249
    - type: mrr_at_1000
      value: 85.252
    - type: mrr_at_3
      value: 84.33800000000001
    - type: mrr_at_5
      value: 84.89
    - type: ndcg_at_1
      value: 76.613
    - type: ndcg_at_10
      value: 84.53399999999999
    - type: ndcg_at_100
      value: 85.359
    - type: ndcg_at_1000
      value: 85.607
    - type: ndcg_at_3
      value: 82.76599999999999
    - type: ndcg_at_5
      value: 83.736
    - type: precision_at_1
      value: 76.613
    - type: precision_at_10
      value: 10.206
    - type: precision_at_100
      value: 1.083
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 31.913000000000004
    - type: precision_at_5
      value: 19.769000000000002
    - type: recall_at_1
      value: 70.97
    - type: recall_at_10
      value: 92.674
    - type: recall_at_100
      value: 95.985
    - type: recall_at_1000
      value: 97.57000000000001
    - type: recall_at_3
      value: 87.742
    - type: recall_at_5
      value: 90.28
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 22.494
    - type: map_at_10
      value: 36.491
    - type: map_at_100
      value: 38.550000000000004
    - type: map_at_1000
      value: 38.726
    - type: map_at_3
      value: 31.807000000000002
    - type: map_at_5
      value: 34.299
    - type: mrr_at_1
      value: 44.907000000000004
    - type: mrr_at_10
      value: 53.146
    - type: mrr_at_100
      value: 54.013999999999996
    - type: mrr_at_1000
      value: 54.044000000000004
    - type: mrr_at_3
      value: 50.952
    - type: mrr_at_5
      value: 52.124
    - type: ndcg_at_1
      value: 44.907000000000004
    - type: ndcg_at_10
      value: 44.499
    - type: ndcg_at_100
      value: 51.629000000000005
    - type: ndcg_at_1000
      value: 54.367
    - type: ndcg_at_3
      value: 40.900999999999996
    - type: ndcg_at_5
      value: 41.737
    - type: precision_at_1
      value: 44.907000000000004
    - type: precision_at_10
      value: 12.346
    - type: precision_at_100
      value: 1.974
    - type: precision_at_1000
      value: 0.246
    - type: precision_at_3
      value: 27.366
    - type: precision_at_5
      value: 19.846
    - type: recall_at_1
      value: 22.494
    - type: recall_at_10
      value: 51.156
    - type: recall_at_100
      value: 77.11200000000001
    - type: recall_at_1000
      value: 93.44
    - type: recall_at_3
      value: 36.574
    - type: recall_at_5
      value: 42.361
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 38.568999999999996
    - type: map_at_10
      value: 58.485
    - type: map_at_100
      value: 59.358999999999995
    - type: map_at_1000
      value: 59.429
    - type: map_at_3
      value: 55.217000000000006
    - type: map_at_5
      value: 57.236
    - type: mrr_at_1
      value: 77.137
    - type: mrr_at_10
      value: 82.829
    - type: mrr_at_100
      value: 83.04599999999999
    - type: mrr_at_1000
      value: 83.05399999999999
    - type: mrr_at_3
      value: 81.904
    - type: mrr_at_5
      value: 82.50800000000001
    - type: ndcg_at_1
      value: 77.137
    - type: ndcg_at_10
      value: 67.156
    - type: ndcg_at_100
      value: 70.298
    - type: ndcg_at_1000
      value: 71.65700000000001
    - type: ndcg_at_3
      value: 62.535
    - type: ndcg_at_5
      value: 65.095
    - type: precision_at_1
      value: 77.137
    - type: precision_at_10
      value: 13.911999999999999
    - type: precision_at_100
      value: 1.6389999999999998
    - type: precision_at_1000
      value: 0.182
    - type: precision_at_3
      value: 39.572
    - type: precision_at_5
      value: 25.766
    - type: recall_at_1
      value: 38.568999999999996
    - type: recall_at_10
      value: 69.56099999999999
    - type: recall_at_100
      value: 81.931
    - type: recall_at_1000
      value: 90.91799999999999
    - type: recall_at_3
      value: 59.358999999999995
    - type: recall_at_5
      value: 64.416
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 88.45600000000002
    - type: ap
      value: 84.09725115338568
    - type: f1
      value: 88.41874909080512
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 21.404999999999998
    - type: map_at_10
      value: 33.921
    - type: map_at_100
      value: 35.116
    - type: map_at_1000
      value: 35.164
    - type: map_at_3
      value: 30.043999999999997
    - type: map_at_5
      value: 32.327
    - type: mrr_at_1
      value: 21.977
    - type: mrr_at_10
      value: 34.505
    - type: mrr_at_100
      value: 35.638999999999996
    - type: mrr_at_1000
      value: 35.68
    - type: mrr_at_3
      value: 30.703999999999997
    - type: mrr_at_5
      value: 32.96
    - type: ndcg_at_1
      value: 21.963
    - type: ndcg_at_10
      value: 40.859
    - type: ndcg_at_100
      value: 46.614
    - type: ndcg_at_1000
      value: 47.789
    - type: ndcg_at_3
      value: 33.007999999999996
    - type: ndcg_at_5
      value: 37.084
    - type: precision_at_1
      value: 21.963
    - type: precision_at_10
      value: 6.493
    - type: precision_at_100
      value: 0.938
    - type: precision_at_1000
      value: 0.104
    - type: precision_at_3
      value: 14.155000000000001
    - type: precision_at_5
      value: 10.544
    - type: recall_at_1
      value: 21.404999999999998
    - type: recall_at_10
      value: 62.175000000000004
    - type: recall_at_100
      value: 88.786
    - type: recall_at_1000
      value: 97.738
    - type: recall_at_3
      value: 40.925
    - type: recall_at_5
      value: 50.722
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 93.50661194710442
    - type: f1
      value: 93.30311193153668
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 73.24669402644778
    - type: f1
      value: 54.23122108002977
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 72.61936785474109
    - type: f1
      value: 70.52644941025565
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 76.76529926025555
    - type: f1
      value: 77.26872729322514
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 33.39450293021839
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 31.757796879839294
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 32.62512146657428
    - type: mrr
      value: 33.84624322066173
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 6.462
    - type: map_at_10
      value: 14.947
    - type: map_at_100
      value: 19.344
    - type: map_at_1000
      value: 20.933
    - type: map_at_3
      value: 10.761999999999999
    - type: map_at_5
      value: 12.744
    - type: mrr_at_1
      value: 47.988
    - type: mrr_at_10
      value: 57.365
    - type: mrr_at_100
      value: 57.931
    - type: mrr_at_1000
      value: 57.96
    - type: mrr_at_3
      value: 54.85
    - type: mrr_at_5
      value: 56.569
    - type: ndcg_at_1
      value: 46.129999999999995
    - type: ndcg_at_10
      value: 38.173
    - type: ndcg_at_100
      value: 35.983
    - type: ndcg_at_1000
      value: 44.507000000000005
    - type: ndcg_at_3
      value: 42.495
    - type: ndcg_at_5
      value: 41.019
    - type: precision_at_1
      value: 47.678
    - type: precision_at_10
      value: 28.731
    - type: precision_at_100
      value: 9.232
    - type: precision_at_1000
      value: 2.202
    - type: precision_at_3
      value: 39.628
    - type: precision_at_5
      value: 35.851
    - type: recall_at_1
      value: 6.462
    - type: recall_at_10
      value: 18.968
    - type: recall_at_100
      value: 37.131
    - type: recall_at_1000
      value: 67.956
    - type: recall_at_3
      value: 11.905000000000001
    - type: recall_at_5
      value: 15.097
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.335
    - type: map_at_10
      value: 46.611999999999995
    - type: map_at_100
      value: 47.632000000000005
    - type: map_at_1000
      value: 47.661
    - type: map_at_3
      value: 41.876999999999995
    - type: map_at_5
      value: 44.799
    - type: mrr_at_1
      value: 34.125
    - type: mrr_at_10
      value: 49.01
    - type: mrr_at_100
      value: 49.75
    - type: mrr_at_1000
      value: 49.768
    - type: mrr_at_3
      value: 45.153
    - type: mrr_at_5
      value: 47.589999999999996
    - type: ndcg_at_1
      value: 34.125
    - type: ndcg_at_10
      value: 54.777
    - type: ndcg_at_100
      value: 58.914
    - type: ndcg_at_1000
      value: 59.521
    - type: ndcg_at_3
      value: 46.015
    - type: ndcg_at_5
      value: 50.861000000000004
    - type: precision_at_1
      value: 34.125
    - type: precision_at_10
      value: 9.166
    - type: precision_at_100
      value: 1.149
    - type: precision_at_1000
      value: 0.121
    - type: precision_at_3
      value: 21.147
    - type: precision_at_5
      value: 15.469
    - type: recall_at_1
      value: 30.335
    - type: recall_at_10
      value: 77.194
    - type: recall_at_100
      value: 94.812
    - type: recall_at_1000
      value: 99.247
    - type: recall_at_3
      value: 54.681000000000004
    - type: recall_at_5
      value: 65.86800000000001
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.62
    - type: map_at_10
      value: 84.536
    - type: map_at_100
      value: 85.167
    - type: map_at_1000
      value: 85.184
    - type: map_at_3
      value: 81.607
    - type: map_at_5
      value: 83.423
    - type: mrr_at_1
      value: 81.36
    - type: mrr_at_10
      value: 87.506
    - type: mrr_at_100
      value: 87.601
    - type: mrr_at_1000
      value: 87.601
    - type: mrr_at_3
      value: 86.503
    - type: mrr_at_5
      value: 87.179
    - type: ndcg_at_1
      value: 81.36
    - type: ndcg_at_10
      value: 88.319
    - type: ndcg_at_100
      value: 89.517
    - type: ndcg_at_1000
      value: 89.60900000000001
    - type: ndcg_at_3
      value: 85.423
    - type: ndcg_at_5
      value: 86.976
    - type: precision_at_1
      value: 81.36
    - type: precision_at_10
      value: 13.415
    - type: precision_at_100
      value: 1.529
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 37.342999999999996
    - type: precision_at_5
      value: 24.534
    - type: recall_at_1
      value: 70.62
    - type: recall_at_10
      value: 95.57600000000001
    - type: recall_at_100
      value: 99.624
    - type: recall_at_1000
      value: 99.991
    - type: recall_at_3
      value: 87.22
    - type: recall_at_5
      value: 91.654
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 60.826438478212744
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 64.24027467551447
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 4.997999999999999
    - type: map_at_10
      value: 14.267
    - type: map_at_100
      value: 16.843
    - type: map_at_1000
      value: 17.229
    - type: map_at_3
      value: 9.834
    - type: map_at_5
      value: 11.92
    - type: mrr_at_1
      value: 24.7
    - type: mrr_at_10
      value: 37.685
    - type: mrr_at_100
      value: 38.704
    - type: mrr_at_1000
      value: 38.747
    - type: mrr_at_3
      value: 34.150000000000006
    - type: mrr_at_5
      value: 36.075
    - type: ndcg_at_1
      value: 24.7
    - type: ndcg_at_10
      value: 23.44
    - type: ndcg_at_100
      value: 32.617000000000004
    - type: ndcg_at_1000
      value: 38.628
    - type: ndcg_at_3
      value: 21.747
    - type: ndcg_at_5
      value: 19.076
    - type: precision_at_1
      value: 24.7
    - type: precision_at_10
      value: 12.47
    - type: precision_at_100
      value: 2.564
    - type: precision_at_1000
      value: 0.4
    - type: precision_at_3
      value: 20.767
    - type: precision_at_5
      value: 17.06
    - type: recall_at_1
      value: 4.997999999999999
    - type: recall_at_10
      value: 25.3
    - type: recall_at_100
      value: 52.048
    - type: recall_at_1000
      value: 81.093
    - type: recall_at_3
      value: 12.642999999999999
    - type: recall_at_5
      value: 17.312
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 85.44942006292234
    - type: cos_sim_spearman
      value: 79.80930790660699
    - type: euclidean_pearson
      value: 82.93400777494863
    - type: euclidean_spearman
      value: 80.04664991110705
    - type: manhattan_pearson
      value: 82.93551681854949
    - type: manhattan_spearman
      value: 80.03156736837379
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 85.63574059135726
    - type: cos_sim_spearman
      value: 76.80552915288186
    - type: euclidean_pearson
      value: 82.46368529820518
    - type: euclidean_spearman
      value: 76.60338474719275
    - type: manhattan_pearson
      value: 82.4558617035968
    - type: manhattan_spearman
      value: 76.57936082895705
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 86.24116811084211
    - type: cos_sim_spearman
      value: 88.10998662068769
    - type: euclidean_pearson
      value: 87.04961732352689
    - type: euclidean_spearman
      value: 88.12543945864087
    - type: manhattan_pearson
      value: 86.9905224528854
    - type: manhattan_spearman
      value: 88.07827944705546
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 84.74847296555048
    - type: cos_sim_spearman
      value: 82.66200957916445
    - type: euclidean_pearson
      value: 84.48132256004965
    - type: euclidean_spearman
      value: 82.67915286000596
    - type: manhattan_pearson
      value: 84.44950477268334
    - type: manhattan_spearman
      value: 82.63327639173352
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 87.23056258027053
    - type: cos_sim_spearman
      value: 88.92791680286955
    - type: euclidean_pearson
      value: 88.13819235461933
    - type: euclidean_spearman
      value: 88.87294661361716
    - type: manhattan_pearson
      value: 88.14212133687899
    - type: manhattan_spearman
      value: 88.88551854529777
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 82.64179522732887
    - type: cos_sim_spearman
      value: 84.25028809903114
    - type: euclidean_pearson
      value: 83.40175015236979
    - type: euclidean_spearman
      value: 84.23369296429406
    - type: manhattan_pearson
      value: 83.43768174261321
    - type: manhattan_spearman
      value: 84.27855229214734
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 88.20378955494732
    - type: cos_sim_spearman
      value: 88.46863559173111
    - type: euclidean_pearson
      value: 88.8249295811663
    - type: euclidean_spearman
      value: 88.6312737724905
    - type: manhattan_pearson
      value: 88.87744466378827
    - type: manhattan_spearman
      value: 88.82908423767314
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 69.91342028796086
    - type: cos_sim_spearman
      value: 69.71495021867864
    - type: euclidean_pearson
      value: 70.65334330405646
    - type: euclidean_spearman
      value: 69.4321253472211
    - type: manhattan_pearson
      value: 70.59743494727465
    - type: manhattan_spearman
      value: 69.11695509297482
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 85.42451709766952
    - type: cos_sim_spearman
      value: 86.07166710670508
    - type: euclidean_pearson
      value: 86.12711421258899
    - type: euclidean_spearman
      value: 86.05232086925126
    - type: manhattan_pearson
      value: 86.15591089932126
    - type: manhattan_spearman
      value: 86.0890128623439
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 87.1976344717285
    - type: mrr
      value: 96.3703145075694
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 59.511
    - type: map_at_10
      value: 69.724
    - type: map_at_100
      value: 70.208
    - type: map_at_1000
      value: 70.22800000000001
    - type: map_at_3
      value: 66.986
    - type: map_at_5
      value: 68.529
    - type: mrr_at_1
      value: 62.333000000000006
    - type: mrr_at_10
      value: 70.55
    - type: mrr_at_100
      value: 70.985
    - type: mrr_at_1000
      value: 71.004
    - type: mrr_at_3
      value: 68.611
    - type: mrr_at_5
      value: 69.728
    - type: ndcg_at_1
      value: 62.333000000000006
    - type: ndcg_at_10
      value: 74.265
    - type: ndcg_at_100
      value: 76.361
    - type: ndcg_at_1000
      value: 76.82900000000001
    - type: ndcg_at_3
      value: 69.772
    - type: ndcg_at_5
      value: 71.94800000000001
    - type: precision_at_1
      value: 62.333000000000006
    - type: precision_at_10
      value: 9.9
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_3
      value: 27.444000000000003
    - type: precision_at_5
      value: 18
    - type: recall_at_1
      value: 59.511
    - type: recall_at_10
      value: 87.156
    - type: recall_at_100
      value: 96.5
    - type: recall_at_1000
      value: 100
    - type: recall_at_3
      value: 75.2
    - type: recall_at_5
      value: 80.661
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.81683168316832
    - type: cos_sim_ap
      value: 95.74716566563774
    - type: cos_sim_f1
      value: 90.64238745574103
    - type: cos_sim_precision
      value: 91.7093142272262
    - type: cos_sim_recall
      value: 89.60000000000001
    - type: dot_accuracy
      value: 99.69405940594059
    - type: dot_ap
      value: 91.09013507754594
    - type: dot_f1
      value: 84.54227113556779
    - type: dot_precision
      value: 84.58458458458459
    - type: dot_recall
      value: 84.5
    - type: euclidean_accuracy
      value: 99.81782178217821
    - type: euclidean_ap
      value: 95.6324301072609
    - type: euclidean_f1
      value: 90.58341862845445
    - type: euclidean_precision
      value: 92.76729559748428
    - type: euclidean_recall
      value: 88.5
    - type: manhattan_accuracy
      value: 99.81980198019802
    - type: manhattan_ap
      value: 95.68510494437183
    - type: manhattan_f1
      value: 90.58945191313342
    - type: manhattan_precision
      value: 93.79014989293361
    - type: manhattan_recall
      value: 87.6
    - type: max_accuracy
      value: 99.81980198019802
    - type: max_ap
      value: 95.74716566563774
    - type: max_f1
      value: 90.64238745574103
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 67.63761899427078
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 36.572473369697235
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 53.63000245208579
    - type: mrr
      value: 54.504193722943725
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 30.300791939416545
    - type: cos_sim_spearman
      value: 31.662904057924123
    - type: dot_pearson
      value: 26.21198530758316
    - type: dot_spearman
      value: 27.006921548904263
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.197
    - type: map_at_10
      value: 1.752
    - type: map_at_100
      value: 10.795
    - type: map_at_1000
      value: 27.18
    - type: map_at_3
      value: 0.5890000000000001
    - type: map_at_5
      value: 0.938
    - type: mrr_at_1
      value: 74
    - type: mrr_at_10
      value: 85.833
    - type: mrr_at_100
      value: 85.833
    - type: mrr_at_1000
      value: 85.833
    - type: mrr_at_3
      value: 85.333
    - type: mrr_at_5
      value: 85.833
    - type: ndcg_at_1
      value: 69
    - type: ndcg_at_10
      value: 70.22
    - type: ndcg_at_100
      value: 55.785
    - type: ndcg_at_1000
      value: 52.93600000000001
    - type: ndcg_at_3
      value: 72.084
    - type: ndcg_at_5
      value: 71.184
    - type: precision_at_1
      value: 74
    - type: precision_at_10
      value: 75.2
    - type: precision_at_100
      value: 57.3
    - type: precision_at_1000
      value: 23.302
    - type: precision_at_3
      value: 77.333
    - type: precision_at_5
      value: 75.6
    - type: recall_at_1
      value: 0.197
    - type: recall_at_10
      value: 2.019
    - type: recall_at_100
      value: 14.257
    - type: recall_at_1000
      value: 50.922
    - type: recall_at_3
      value: 0.642
    - type: recall_at_5
      value: 1.043
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 2.803
    - type: map_at_10
      value: 10.407
    - type: map_at_100
      value: 16.948
    - type: map_at_1000
      value: 18.424
    - type: map_at_3
      value: 5.405
    - type: map_at_5
      value: 6.908
    - type: mrr_at_1
      value: 36.735
    - type: mrr_at_10
      value: 50.221000000000004
    - type: mrr_at_100
      value: 51.388
    - type: mrr_at_1000
      value: 51.402
    - type: mrr_at_3
      value: 47.278999999999996
    - type: mrr_at_5
      value: 49.626
    - type: ndcg_at_1
      value: 34.694
    - type: ndcg_at_10
      value: 25.507
    - type: ndcg_at_100
      value: 38.296
    - type: ndcg_at_1000
      value: 49.492000000000004
    - type: ndcg_at_3
      value: 29.006999999999998
    - type: ndcg_at_5
      value: 25.979000000000003
    - type: precision_at_1
      value: 36.735
    - type: precision_at_10
      value: 22.041
    - type: precision_at_100
      value: 8.02
    - type: precision_at_1000
      value: 1.567
    - type: precision_at_3
      value: 28.571
    - type: precision_at_5
      value: 24.490000000000002
    - type: recall_at_1
      value: 2.803
    - type: recall_at_10
      value: 16.378
    - type: recall_at_100
      value: 50.489
    - type: recall_at_1000
      value: 85.013
    - type: recall_at_3
      value: 6.505
    - type: recall_at_5
      value: 9.243
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 70.55579999999999
    - type: ap
      value: 14.206982753316227
    - type: f1
      value: 54.372142814964285
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 56.57611771363893
    - type: f1
      value: 56.924172639063144
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 52.82304915719759
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 85.92716218632653
    - type: cos_sim_ap
      value: 73.73359122546046
    - type: cos_sim_f1
      value: 68.42559487116262
    - type: cos_sim_precision
      value: 64.22124508215691
    - type: cos_sim_recall
      value: 73.21899736147758
    - type: dot_accuracy
      value: 80.38981939560112
    - type: dot_ap
      value: 54.61060862444974
    - type: dot_f1
      value: 53.45710627400769
    - type: dot_precision
      value: 44.87638839125761
    - type: dot_recall
      value: 66.09498680738787
    - type: euclidean_accuracy
      value: 86.02849138701794
    - type: euclidean_ap
      value: 73.95673761922404
    - type: euclidean_f1
      value: 68.6783042394015
    - type: euclidean_precision
      value: 65.1063829787234
    - type: euclidean_recall
      value: 72.66490765171504
    - type: manhattan_accuracy
      value: 85.9808070572808
    - type: manhattan_ap
      value: 73.9050720058029
    - type: manhattan_f1
      value: 68.57560618983794
    - type: manhattan_precision
      value: 63.70839936608558
    - type: manhattan_recall
      value: 74.24802110817942
    - type: max_accuracy
      value: 86.02849138701794
    - type: max_ap
      value: 73.95673761922404
    - type: max_f1
      value: 68.6783042394015
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 88.72783017037295
    - type: cos_sim_ap
      value: 85.52705223340233
    - type: cos_sim_f1
      value: 77.91659078492079
    - type: cos_sim_precision
      value: 73.93378032764221
    - type: cos_sim_recall
      value: 82.35294117647058
    - type: dot_accuracy
      value: 85.41739434159972
    - type: dot_ap
      value: 77.17734818118443
    - type: dot_f1
      value: 71.63473589973144
    - type: dot_precision
      value: 66.96123719622415
    - type: dot_recall
      value: 77.00954727440714
    - type: euclidean_accuracy
      value: 88.68125897465751
    - type: euclidean_ap
      value: 85.47712213906692
    - type: euclidean_f1
      value: 77.81419950830664
    - type: euclidean_precision
      value: 75.37162649733006
    - type: euclidean_recall
      value: 80.42038805050817
    - type: manhattan_accuracy
      value: 88.67349710870494
    - type: manhattan_ap
      value: 85.46506475241955
    - type: manhattan_f1
      value: 77.87259084890393
    - type: manhattan_precision
      value: 74.54929577464789
    - type: manhattan_recall
      value: 81.50600554357868
    - type: max_accuracy
      value: 88.72783017037295
    - type: max_ap
      value: 85.52705223340233
    - type: max_f1
      value: 77.91659078492079
language:
- en
license: mit
---

# gte-large

General Text Embeddings (GTE) model. [Towards General Text Embeddings with Multi-stage Contrastive Learning](https://arxiv.org/abs/2308.03281)

The GTE models are trained by Alibaba DAMO Academy. They are mainly based on the BERT framework and currently offer three different sizes of models, including [GTE-large](https://huggingface.co/thenlper/gte-large), [GTE-base](https://huggingface.co/thenlper/gte-base), and [GTE-small](https://huggingface.co/thenlper/gte-small). The GTE models are trained on a large-scale corpus of relevance text pairs, covering a wide range of domains and scenarios. This enables the GTE models to be applied to various downstream tasks of text embeddings, including **information retrieval**, **semantic textual similarity**, **text reranking**, etc.

## Metrics

We compared the performance of the GTE models with other popular text embedding models on the MTEB benchmark. For more detailed comparison results, please refer to the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).



| Model Name | Model Size (GB) | Dimension | Sequence Length | Average (56) | Clustering (11) | Pair Classification (3) | Reranking (4) | Retrieval (15) | STS (10) | Summarization (1) | Classification (12) |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**gte-large**](https://huggingface.co/thenlper/gte-large) | 0.67 | 1024 | 512 | **63.13** | 46.84 | 85.00 | 59.13 | 52.22 | 83.35 | 31.66 | 73.33 |
| [**gte-base**](https://huggingface.co/thenlper/gte-base) 	| 0.22 | 768 | 512 | **62.39** | 46.2 | 84.57 | 58.61 | 51.14 | 82.3 | 31.17 | 73.01 |
| [e5-large-v2](https://huggingface.co/intfloat/e5-large-v2) | 1.34 | 1024| 512 | 62.25 | 44.49 | 86.03 | 56.61 | 50.56 | 82.05 | 30.19 | 75.24 |
| [e5-base-v2](https://huggingface.co/intfloat/e5-base-v2) | 0.44 | 768 | 512 | 61.5 | 43.80 | 85.73 | 55.91 | 50.29 | 81.05 | 30.28 | 73.84 |
| [**gte-small**](https://huggingface.co/thenlper/gte-small) | 0.07 | 384 | 512 | **61.36** | 44.89 | 83.54 | 57.7 | 49.46 | 82.07 | 30.42 | 72.31 |
| [text-embedding-ada-002](https://platform.openai.com/docs/guides/embeddings) | - | 1536 | 8192 | 60.99 | 45.9 | 84.89 | 56.32 | 49.25 | 80.97 | 30.8 | 70.93 |
| [e5-small-v2](https://huggingface.co/intfloat/e5-base-v2) | 0.13 | 384 | 512 | 59.93 | 39.92 | 84.67 | 54.32 | 49.04 | 80.39 | 31.16 | 72.94 |
| [sentence-t5-xxl](https://huggingface.co/sentence-transformers/sentence-t5-xxl) | 9.73 | 768 | 512 | 59.51 | 43.72 | 85.06 | 56.42 | 42.24 | 82.63 | 30.08 | 73.42 |
| [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) 	| 0.44 | 768 | 514 	| 57.78 | 43.69 | 83.04 | 59.36 | 43.81 | 80.28 | 27.49 | 65.07 |
| [sgpt-bloom-7b1-msmarco](https://huggingface.co/bigscience/sgpt-bloom-7b1-msmarco) 	| 28.27 | 4096 | 2048 | 57.59 | 38.93 | 81.9 | 55.65 | 48.22 | 77.74 | 33.6 | 66.19 |
| [all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) 	| 0.13 | 384 | 512 	| 56.53 | 41.81 | 82.41 | 58.44 | 42.69 | 79.8 | 27.9 | 63.21 |
| [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) 	| 0.09 | 384 | 512 	| 56.26 | 42.35 | 82.37 | 58.04 | 41.95 | 78.9 | 30.81 | 63.05 |
| [contriever-base-msmarco](https://huggingface.co/nthakur/contriever-base-msmarco) 	| 0.44 | 768 | 512 	| 56.00 | 41.1 	| 82.54 | 53.14 | 41.88 | 76.51 | 30.36 | 66.68 |
| [sentence-t5-base](https://huggingface.co/sentence-transformers/sentence-t5-base) 	| 0.22 | 768 | 512 	| 55.27 | 40.21 | 85.18 | 53.09 | 33.63 | 81.14 | 31.39 | 69.81 |


## Usage

Code example

```python
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]

tokenizer = AutoTokenizer.from_pretrained("thenlper/gte-large")
model = AutoModel.from_pretrained("thenlper/gte-large")

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# (Optionally) normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
print(scores.tolist())
```

Use with sentence-transformers:
```python
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

sentences = ['That is a happy person', 'That is a very happy person']

model = SentenceTransformer('thenlper/gte-large')
embeddings = model.encode(sentences)
print(cos_sim(embeddings[0], embeddings[1]))
```

### Limitation

This model exclusively caters to English texts, and any lengthy texts will be truncated to a maximum of 512 tokens.

### Citation

If you find our paper or models helpful, please consider citing them as follows:

```
@misc{li2023general,
      title={Towards General Text Embeddings with Multi-stage Contrastive Learning}, 
      author={Zehan Li and Xin Zhang and Yanzhao Zhang and Dingkun Long and Pengjun Xie and Meishan Zhang},
      year={2023},
      eprint={2308.03281},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
