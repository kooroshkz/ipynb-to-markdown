## Introduction to Propositional Logic

### Dictionary

| Word | Defenition          |
|------------|---------------|
| Proposition | A statement that expresses a judgment or opinion.     |
| Absurdity   | Meaningless                                           |
| Conventions | An agreement between people that assumes something.   |
| Derive      | obtain or receive something from a source or origin   |


| Connective | Name          | Pronunciation | Intuitive Meaning                          |
|------------|---------------|---------------|--------------------------------------------|
| ⊥          | Absurdity     | bottom        | ⊥ never holds (e.g., "The sky is blue and not blue" -> logically false) |
| ∧          | Conjunction   | and           | Both hold                                  |
| ∨          | Disjunction   | or            | φ or ψ or both hold                        |
| →          | Implication   | φ implies ψ   | If φ holds, then ψ holds                   |
| ¬φ         | Negation      | φ -> ⊥        |                                            |
| ⊤          | Truth or Top  | ¬⊥            | Always true (e.g., "A triangle has 3 vertices")|
| φ ↔ ψ      | Bi-implication|(φ -> ψ) ∧ (ψ -> φ)| True when both are same        |




| Connective | Equivalent          | Contradiction |
|------------|---------------|---------------|
| $p \to q$  |$\neg p \lor q$   | $ p \land \neg q$ |
| $\neg(p \to q)$ | $ p \land \neg q$   | $\neg p \lor q$  |



In the parse tree, ¬p will always be p → ⊥.

φ = q ∧ ~p → r → s = ( q ∧ ( p → ⊥ ) ) → ( r → s )
Sub(φ) = { φ, r, p, q, s, ⊥,
p → ⊥, q ∧ ( p → ⊥ ), r → s } 

Top-level connective: ∧ 

Direct subformulas: p, q 

Atomic formula: ⊥ 

Subformulas of 𝜑: all the formulas that appear in the parse tree of 𝜑, including 𝜑 itself  

Set of maps (𝐵^𝐴): 𝐴 → 𝐵 

Powerset: P(𝐴) = {𝑈 | 𝑈 ⊆ 𝐴} 

Natural Numbers: [𝑛] = {𝑘 ∈ N | 𝑘 < 𝑛} [0] = ∅, [1] = {0}

