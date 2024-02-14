Association discovery is commonly called Market Basket Analysis (MBA). MBA is widely used by grocery stores, banks, and telecommunications among others. Its results are used to optimize store layouts, design product bundles, plan coupon offers, choose appropriate specials and choose attached mailing in direct marketing. The MBA helps us to understand what items are likely to be purchased together. On-line transaction processing systems often provide the data sources for association discovery
Basic Concepts for Association Discovery An association rule is written A => B where A is the antecedent and B is the consequent. Both sides of an association rule can contain more than one item. Techniques used in Association discovery are borrowed from probability and statistics. Support, confidence, and Lift are three important evaluation criteria of association discovery.

A. Support The level of support is how frequently the combination occurs in the market basket (database). Support is the percentage of baskets (or transactions) that contain both A and B of the association, i.e. % of baskets where the rule is true

Support(A => B) = P(A ∩ B)

B. Expected confidence This is the probability of the consequent if it was independent of the antecedent. Expected confidence is thus the percentage of occurrences containing B

Expected confidence (A => B) = P(B)

Confidence The strength of an association is defined by its confidence factor, which is the percentage of cases in which a consequent appears given that the antecedent has occurred. Confidence is the percentage of baskets having A that also contain B, i.e. % of baskets containing B among those containing A. Note: Confidence(A => B) ≠ Confidence(B => A).

Confidence(A => B) = P(B | A)

C. Lift

Lift is equal to the confidence factor divided by the expected confidence. Lift is a factor by which the likelihood of consequent increases given an antecedent. Expected confidence is equal to the number of consequent transactions divided by the total number of transactions. Lift is the ratio of the likelihood of finding B in a basket known to contain A, to the likelihood of finding B in any random basket.
