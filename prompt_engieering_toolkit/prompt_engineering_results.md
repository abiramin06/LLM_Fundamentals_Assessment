Prompt Engineering Toolkit – Classification Experiment

Objective

To compare three prompting techniques for classifying 15 customer support tickets into categories and priorities.

Results

Prompt Version| Technique| Correct| Total| Accuracy
Version 1| Basic Prompt| 13| 15| 86.67%
Version 2| Role, Task, Constraints, Output Format| 12| 15| 80.00%
Version 3| Few-Shot Prompting| 12| 15| 80.00%

Observations

- Version 1 achieved the highest accuracy at 86.67%.
- Version 2 achieved 80% accuracy.
- Version 3 also achieved 80% accuracy.
- Adding more instructions or examples did not improve accuracy in this experiment.
- The results show that prompt quality should be evaluated using actual test data rather than assumptions.

Conclusion

The basic prompt performed best on this particular test set. Further improvements could include clearer priority definitions, better examples, and reviewing incorrectly classified tickets.
