# Section-by-Section Examples

This file contains rewrite examples for common paper sections. Each example shows a before/after pair plus a Chinese note explaining what changed.

Use these as patterns. Do not copy phrases verbatim across papers.

---

## 1. Method Section

**Before (AI-flavored):**

> In this work, we comprehensively investigate a novel deep learning framework that seamlessly integrates a fuzzy neural network with a robust feature extractor. It is worth noting that our approach plays a crucial role in mitigating the inherent challenges of high-dimensional feature spaces.

**After (de-AI):**

> We build the framework around a fuzzy neural network coupled with a feature extractor tuned for high-dimensional inputs. The coupling is intentional. A standalone extractor tends to overfit narrow feature bands, while the fuzzy layer absorbs uncertainty in the membership boundary, which is what makes the joint design useful in practice.

**结构调整说明（中文）：**

- 删除 "comprehensively / seamlessly / crucial / It is worth noting" 等 AI 痕迹词。
- 用一短句 "The coupling is intentional." 制造节奏断点（burstiness）。
- 增加因果链解释，让方法选择带有“真实实验权衡”的痕迹。
- 保留 fuzzy neural network 等术语原样。

---

## 2. Experiment Setup

**Before:**

> All experiments are conducted in a Python environment. We adopt a 5-fold cross-validation strategy to comprehensively evaluate the performance of our model. The learning rate is carefully tuned to ensure optimal results.

**After:**

> All experiments run in Python. We use 5-fold cross-validation to estimate variance across splits rather than to maximize a single best score. The learning rate is selected from a small grid; we report the value that gives the most stable validation curve, not the lowest single-fold loss.

**结构调整说明（中文）：**

- 把“comprehensively evaluate / carefully tuned / optimal results”这种空泛措辞换成可解释的实验意图。
- `5-fold cross-validation`、`Python` 等术语原样保留。
- 把通用句拆成一短一长，节奏更人写。
- 加入“为什么这样选”的隐含理由，提升人类痕迹。

---

## 3. Results / Discussion

**Before:**

> The results demonstrate that our method significantly outperforms existing baselines, achieving state-of-the-art performance and showcasing its robustness across diverse datasets.

**After:**

> Our method outperforms the listed baselines on every dataset we tested. The margin is largest on the noisy subset, where baseline accuracy drops sharply; this is consistent with the design intent, since the fuzzy layer is specifically meant to dampen membership noise rather than improve clean-data accuracy.

**结构调整说明（中文）：**

- 删除 "significantly / state-of-the-art / showcasing / robustness" 等典型 AI 套话。
- 把“在所有数据集都更好”转成“在哪个子集差距最大 + 为什么”，体现人类作者会做的细致解释。
- 用半冒号长句承载因果说明，而不是堆叠短赞美句。

---

## 4. Abstract Snippet

**Before:**

> In this paper, we propose a novel framework that comprehensively addresses the challenges of high-dimensional data, demonstrating significantly improved performance over state-of-the-art methods.

**After:**

> We present a framework for high-dimensional inputs where the bottleneck is membership uncertainty rather than raw feature count. On three benchmarks the proposed model improves over the strongest prior method, with the gain concentrated in low signal-to-noise regions.

**结构调整说明（中文）：**

- 删除 "novel / comprehensively / significantly improved / state-of-the-art" 词组。
- 把贡献从“全面更好”收缩到一个具体瓶颈和具体增益区间。
- 替换“we propose”为“We present”，避免 AI 模板开头。

---

## 5. Related Work

**Before:**

> Numerous studies have delved into this area, paving the way for groundbreaking advancements. However, existing methods often fall short in addressing the inherent challenges.

**After:**

> Prior work in this area can be grouped along two axes: feature-side modeling and decision-side calibration. Both lines have produced strong results on clean benchmarks, yet performance under heavy label noise remains the open issue we target here.

**结构调整说明（中文）：**

- 删除 "delved into / paving the way / groundbreaking" 等高 AI 风险表达。
- 用“两条主线”这种学者常见的归类法重写，更像 reviewer 思路。
- 直接交代“没解决的问题点”，自然引出本文动机。

---

## 6. Limitations

**Before:**

> While our method demonstrates remarkable performance, it is not without limitations.

**After:**

> Two limits are worth flagging. First, the fuzzy layer adds non-trivial training cost on very large vocabularies. Second, our analysis assumes membership noise is bounded; under unbounded noise the dampening behavior is no longer guaranteed.

**结构调整说明（中文）：**

- 删除 "remarkable / not without limitations" 这种掩饰性 AI 表达。
- 用“flagging two limits”这种作者口吻，并各给一个具体边界条件。
- 让 limitations 段落具备技术可证伪性，而不是公式化套话。

---

## How to Apply

1. Pick the section type matching your text.
2. Compare your draft with the "Before" pattern above.
3. If your draft contains the same AI-trace words/phrases, rewrite using the "After" style.
4. Run the self-check from `reference.md` before finalizing.
