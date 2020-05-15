# Active test folder

**THIS FOLDER IS NOT NEEDED TO BE DEPLOYIED TO PRODUCTION**

Some part of the system must make a real connect to AWS apis.

So, it's not a isolated test as a *unit test* should be. By the other hand, also does not integrates to the whole application rules, so we may not also say that we are talking about *integration test* as well.

Then I call it as *active test*. This is much like as unit test, but with a real integration with AWS apis. I will make it very clear that a mere connection to some real resource does not transforms a test into an integration test, indeed. Another thing that make it more similar to an unittest in that we are really testing the tiniest and deepest part from the system, but with a real connection. And results and health of such tests will ensure that the general top level application will not have issues in places where it is hard to troubeshoot (an aspect that is tha same that a unit test do).

We will not use the python unit tests features. So the result will generaly print outputs, so further checks and exams in the depest application level will be possible without manual testing in the full application.


