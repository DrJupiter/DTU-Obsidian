
# Experiment design with blocks

## plus minus method

This is about doing designs with a lack of materials.
We run these experiments in blocks and we want to confound the higher order effect (combinations) with the blocks themselves.
We do this by making all types of the higher order effects be grouped together when they are the same in respective blocks.
Fx if the algebra gives us -1 and +1 values for the effects, then all the +1 effects should be in one block for the effect and all the -1 effects in another.
Ex
![[Pasted image 20241027202409.png]]

Here ABC is confounded with the blocks 1 and 2, so we can't tell the difference between that effect and the block effects.

## linear combination method

**General Formulation for Constructing Blocks Using Defining Contrasts in Factorial Designs**

In factorial experiments, especially those involving a large number of factors, it is often necessary to partition the treatment combinations into blocks to control for variability and improve experimental efficiency. One systematic method for constructing these blocks is through the use of **defining contrasts** based on linear combinations of the factor levels.

**General Method:**

1. **Define the Factors and Their Levels:**
   - Consider a factorial experiment with  $k$ factors.
   - Each factor  $i$ has  $s_i$ levels, which can be coded as integers from  $0$ to $s_i - 1$.

2. **Select the Modulus:**
   - Choose a modulus $m$ based on the levels of the factors and the desired number of blocks. For simplicity, when all factors have the same number of levels $s$, set $m = s$.

3. **Construct Defining Contrasts:**
   - Define one or more linear combinations (defining contrasts) of the form:
     $$
     L_j = \sum_{i=1}^{k} \delta_{ji} x_i \mod m, \quad \text{for } j = 1, 2, \dots, t
     $$
     where:
     -$x_i$ is the coded level of factor $i$ in a treatment combination.
     - $\delta_{ji}$ are integers (coefficients) that determine the specific effects to be confounded. These coefficients are selected from  $0$ to $m - 1$.
     - $t$ is the number of defining contrasts used, which depends on the number of blocks desired.

4. **Assign Treatment Combinations to Blocks:**
   - Calculate the values of $L_j$ for each treatment combination.
   - Treatment combinations that yield the same set of values $(L_1, L_2, \dots, L_t)$ are placed in the same block.

**Key Points:**

- The coefficients $\delta_{ji}$ determine which interactions or effects are confounded with blocks.
- The method ensures that the treatment combinations are systematically and evenly distributed across the blocks.
- By adjusting the number and form of the defining contrasts, you can control the size and number of blocks.

**Example for a $2^k$ Factorial Design:**

- **Factors and Levels:**
  - $k$ factors, each at 2 levels (coded as 0 and 1).

- **Modulus:**
  - $m = 2$.

- **Defining Contrast:**
  - A single defining contrast:
    $$ L = \sum_{i=1}^{k} \delta_i x_i \mod 2 $$
    where $\delta_i \in \{0, 1\}$.

- **Block Assignment:**
  - Treatment combinations with $L = 0$ are placed in one block.
  - Those with $L = 1$ are placed in the other block.

**Generalization to $s^k$ Factorial Designs:**

- For factors at $s$ levels, coded from $0$ to $s - 1$, and modulus $m = s$, the method extends naturally.
- Multiple defining contrasts can be used to create more than two blocks, allowing for greater flexibility in experimental design.

**Summary:**

The general formulation for constructing blocks using defining contrasts involves:

- Coding factor levels numerically.
- Selecting appropriate coefficients to define the contrasts.
- Using modular arithmetic to group treatment combinations into blocks based on the calculated contrast values.

This method provides a systematic approach to block construction, ensuring balanced and efficient experimental designs.

### when $m\neq s$

**Handling the Case When Modulus $m$ Does Not Equal the Number of Levels $s$**

In the general formulation for constructing blocks using defining contrasts in factorial designs, the modulus $m$ does not necessarily have to equal the number of levels $s$ of the factors. Choosing $m \neq s$ can offer greater flexibility in designing experiments, allowing for different block sizes, numbers of blocks, and confounding patterns.

---

#### **General Method with $m \ne s$:**

1. **Define Factors and Levels:**
   - **Factors:** Consider $k$ factors.
   - **Levels:** Each factor $i$ has $s_i$ levels, coded numerically from $0$ to $s_i - 1$.
   - **Treatment Combinations:** All possible combinations of factor levels form the treatment combinations.

2. **Select Modulus $m$:**
   - **Choice of $m$:** Choose a positive integer $m$ that suits the desired blocking structure. It does not have to equal any $s_i$.
   - **Considerations for $m$:**
     - $m$ can be any integer, but it's often practical to choose $m$ as a divisor of the total number of treatment combinations for balanced blocks.
     - The modulus $m$ determines the number of distinct values the defining contrasts can take and thus the number of blocks.

3. **Construct Defining Contrasts:**
   - **Defining Contrasts:** One or more linear combinations are defined as:
     $$
     L_j = \sum_{i=1}^{k} \delta_{ji} x_i \mod m, \quad \text{for } j = 1, 2, \dots, t
     $$
     where:
     - $x_i$ is the coded level of factor $i$.
     - $\delta_{ji}$ are integer coefficients (contrast coefficients).
     - $t$ is the number of defining contrasts, determining the blocking structure.

4. **Assign Treatment Combinations to Blocks:**
   - **Compute $L_j$:** Calculate the values of $L_j$ for each treatment combination.
   - **Block Assignment:** Group treatment combinations into blocks based on their $(L_1, L_2, \dots, L_t)$ values.
     - The number of blocks is $m^t$ if all combinations of $L_j$ values are possible.
     - Blocks consist of treatments sharing the same $L_j$ values.

---

#### **Key Considerations When $m \ne s$:**

1. **Flexibility in Blocking:**
   - Choosing $m \neq s$ allows for different numbers of blocks and block sizes, which can be tailored to practical constraints like available resources or experimental units.

2. **Effect of Modulus on Confounding:**
   - The modulus $m$ influences which interactions or effects are confounded with blocks.
   - By carefully selecting $m$ and the coefficients $\delta_{ji}$, you can control the confounding pattern to keep important effects unconfounded.

3. **Compatibility of Factor Levels and Modulus:**
   - When $s_i > m$, the levels of some factors will wrap around under modulo $m$ arithmetic.
   - Ensure that this wrapping does not inadvertently group dissimilar treatment combinations or confound critical effects.

4. **Treatment of Non-Integer Levels:**
   - If factor levels are not integers or are coded differently, adjust the coding scheme to align with the modulus $m$ used.

---

#### **Examples Illustrating $m \ne s$:**

#### **Example 1: $2^3$ Factorial Design with Modulus $m = 4$:**

- **Factors and Levels:**
  - Three factors $A$, $B$, $C$, each at 2 levels (coded 0 and 1).
- **Modulus:**
  - $m = 4$.
- **Defining Contrast:**
  - $L = x_A + 2x_B + 3x_C \mod 4$.
- **Calculation of $L$:**
  - Compute $L$ for each treatment combination.
- **Block Assignment:**
  - Treatment combinations are assigned to 4 blocks based on $L$ values (0, 1, 2, 3).
- **Implications:**
  - With $m = 4$, we have more blocks than levels per factor.
  - Specific higher-order interactions may be confounded with blocks depending on the coefficients.

#### **Example 2: $3^2$ Factorial Design with Modulus $m = 2$:**

- **Factors and Levels:**
  - Two factors $A$, $B$, each at 3 levels (coded 0, 1, 2).
- **Modulus:**
  - $m = 2$.
- **Defining Contrast:**
  - $L = x_A + x_B \mod 2$.
- **Calculation of $L$:**
  - Since factor levels exceed $m$, values of $x_i$ wrap around under modulo 2.
- **Block Assignment:**
  - Treatment combinations are split into 2 blocks based on $L$ values (0 or 1).
- **Implications:**
  - Despite 3 levels per factor, using $m = 2$ simplifies the blocking into 2 blocks.
  - Some effects may be aliased differently than if $m = 3$.

---

#### **Practical Guidelines for Using $m \ne s$:**

1. **Design Objectives:**
   - Determine the primary goals of your experiment (e.g., minimizing block size, controlling confounding).
   - Choose $m$ to align with these objectives.

2. **Selecting Coefficients $\delta_{ji}$:**
   - Choose coefficients to avoid confounding critical main effects or low-order interactions.
   - Use orthogonality principles where possible to maintain balance.

3. **Ensuring Balanced Blocks:**
   - Verify that the number of treatment combinations is divisible by the number of blocks to maintain equal block sizes.
   - If not, be prepared to handle unbalanced blocks or adjust the design.

4. **Analyzing Confounding Patterns:**
   - Use the defining contrasts to derive the alias structure of the design.
   - Identify which effects are confounded with blocks and adjust the analysis accordingly.

5. **Modular Arithmetic Considerations:**
   - Be mindful of how factor levels interact under the chosen modulus.
   - Ensure that the modulo operation leads to meaningful distinctions between treatment combinations.

---

#### **Advantages of Using $m \ne s$:**

- **Customized Blocking Structures:**
  - Tailor the number and size of blocks to experimental constraints.
- **Control Over Confounding:**
  - Greater flexibility in deciding which effects are confounded with blocks.
- **Accommodating Mixed-Level Designs:**
  - Suitable for designs where factors have different numbers of levels.

---

#### **Conclusion:**

Using a modulus $m$ that does not equal the number of levels $s$ of the factors expands the versatility of block construction in factorial designs. It allows experimenters to:

- Design experiments with a number of blocks different from the number of factor levels.
- Confound specific higher-order interactions with blocks while keeping essential effects unconfounded.
- Adjust block sizes to match practical limitations or resource availability.

By carefully selecting the modulus $m$ and the defining contrasts, you can create a factorial design that meets your experimental needs while maintaining control over the confounding structure and ensuring efficient use of resources.

---

**Remember:** When $m \neq s$, it's crucial to thoroughly analyze the alias structure and understand how the chosen modulus and defining contrasts affect the confounding of effects. This understanding ensures accurate interpretation of experimental results and valid conclusions .

