"""
This script uses mturk's API to create a new HIT with tailor made test question as qualification
"""

import boto3
import pickle
import pandas as pd
import random
from tqdm import tqdm


sandbox_host = 'mechanicalturk.sandbox.amazonaws.com'
region_name = 'us-east-1'
aws_access_key_id = ""
aws_secret_access_key = ""
endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
# Uncomment this line to use in production
#endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'


#################### Qualifications ####################
def def_questions():
    """
    Test questions
    """
    questions = """
    <QuestionForm xmlns='http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2017-11-06/QuestionForm.xsd'>
      <Question>
          <QuestionIdentifier>Query1</QuestionIdentifier>
          <DisplayName> Pigeons' discrimination of paintings by Monet and Picasso </DisplayName>
          <IsRequired>true</IsRequired>
          <QuestionContent>
  <EmbeddedBinary>
      <EmbeddedMimeType>
            <Type>image</Type>
            <SubType>png</SubType>
  </EmbeddedMimeType>
          <DataURL>https://www.cse.huji.ac.il/~chenxshani/inst.png</DataURL>
          <AltText>Instructions</AltText>
           <Width>1270</Width>
           <Height>1074</Height>
        </EmbeddedBinary>
    <Text>
    "Pigeons' discrimination of paintings by Monet and Picasso"
    How funny is the title of this paper?
    </Text>
          </QuestionContent>
          <AnswerSpecification>
            <SelectionAnswer>
              <StyleSuggestion>radiobutton</StyleSuggestion>
              <Selections>
                <Selection>
                  <SelectionIdentifier>A1</SelectionIdentifier>
                  <Text>1 - Not funny</Text>
                </Selection>
                <Selection>
                  <SelectionIdentifier>A2</SelectionIdentifier>
                  <Text>2</Text>
                </Selection>
                <Selection>
                  <SelectionIdentifier>A3</SelectionIdentifier>
                  <Text>3 - Somewhat funny</Text>
                </Selection>
                <Selection>
                  <SelectionIdentifier>A4</SelectionIdentifier>
                  <Text>4</Text>
                </Selection>
                  <Selection>
                  <SelectionIdentifier>A5</SelectionIdentifier>
                  <Text>5 - Funny</Text>
                </Selection>
              </Selections>
            </SelectionAnswer>
          </AnswerSpecification>
      </Question>
      <Question>
    
    <QuestionIdentifier>Query2</QuestionIdentifier>
    <DisplayName> Pigeons' discrimination of paintings by Monet and Picasso </DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
        <Text>
        "Pigeons' discrimination of paintings by Monet and Picasso"
        How funny is the topic of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A21</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                     <Selection>
                      <SelectionIdentifier>A22</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A23</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A24</SelectionIdentifier>
                      <Text>4</Text>
                        </Selection>
                    <Selection>
                      <SelectionIdentifier>A25</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
    <Question>
      <QuestionIdentifier>Query3</QuestionIdentifier>
      <DisplayName> Elucidation of Chemical Compounds Responsible for Foot Malodour </DisplayName>
      <IsRequired>true</IsRequired>
      <QuestionContent>
        <Text>
        "Elucidation of Chemical Compounds Responsible for Foot Malodour"
        How funny is the title of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A31</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A32</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A33</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A34</SelectionIdentifier>
                      <Text>4</Text>
                    </Selection>
                      <Selection>
                      <SelectionIdentifier>A35</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
          <Question>
    
    <QuestionIdentifier>Query4</QuestionIdentifier>
    <DisplayName> Elucidation of Chemical Compounds Responsible for Foot Malodour </DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
        <Text>
        "Elucidation of Chemical Compounds Responsible for Foot Malodour"
        How funny is the topic of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A41</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                     <Selection>
                      <SelectionIdentifier>A42</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A43</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A44</SelectionIdentifier>
                      <Text>4</Text>
                        </Selection>
                    <Selection>
                      <SelectionIdentifier>A45</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
    <Question>
      <QuestionIdentifier>Query7</QuestionIdentifier>
      <DisplayName> Hippocampal Subfield Volumes in Mood Disorders. </DisplayName>
      <IsRequired>true</IsRequired>
      <QuestionContent>
        <Text>
        "Hippocampal Subfield Volumes in Mood Disorders."
        How funny is the title of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A71</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A72</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A73</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A74</SelectionIdentifier>
                      <Text>4</Text>
                    </Selection>
                      <Selection>
                      <SelectionIdentifier>A75</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
    <Question>
      <QuestionIdentifier>Query8</QuestionIdentifier>
      <DisplayName>Hippocampal Subfield Volumes in Mood Disorders. </DisplayName>
      <IsRequired>true</IsRequired>
      <QuestionContent>
        <Text>
        "Hippocampal Subfield Volumes in Mood Disorders."
        How funny is the topic of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A81</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A82</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A83</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A84</SelectionIdentifier>
                      <Text>4</Text>
                    </Selection>
                      <Selection>
                      <SelectionIdentifier>A85</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
 <Question>
    <QuestionIdentifier>Query11</QuestionIdentifier>
    <DisplayName> A Preliminary Survey of Rhinotillexomania in an Adolescent Sample for their probing medical discovery that nose picking is a common activity among adolescents. </DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
        <Text>
        "A Preliminary Survey of Rhinotillexomania in an Adolescent Sample for their probing medical discovery that nose picking is a common activity among adolescents. "
        How funny is the title of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A111</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A112</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A113</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A114</SelectionIdentifier>
                      <Text>4</Text>
                    </Selection>
                      <Selection>
                      <SelectionIdentifier>A115</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
    <Question>
      <QuestionIdentifier>Query12</QuestionIdentifier>
      <DisplayName>A Preliminary Survey of Rhinotillexomania in an Adolescent Sample for their probing medical discovery that nose picking is a common activity among adolescents. </DisplayName>
      <IsRequired>true</IsRequired>
      <QuestionContent>
        <Text>
        "A Preliminary Survey of Rhinotillexomania in an Adolescent Sample for their probing medical discovery that nose picking is a common activity among adolescents."
        How funny is the topic of this paper?
        </Text>
              </QuestionContent>
              <AnswerSpecification>
                <SelectionAnswer>
                  <StyleSuggestion>radiobutton</StyleSuggestion>
                  <Selections>
                    <Selection>
                      <SelectionIdentifier>A121</SelectionIdentifier>
                      <Text>1 - Not funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A122</SelectionIdentifier>
                      <Text>2</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A123</SelectionIdentifier>
                      <Text>3 - Somewhat funny</Text>
                    </Selection>
                    <Selection>
                      <SelectionIdentifier>A124</SelectionIdentifier>
                      <Text>4</Text>
                    </Selection>
                      <Selection>
                      <SelectionIdentifier>A125</SelectionIdentifier>
                      <Text>5 - Funny</Text>
                    </Selection>
                  </Selections>
                </SelectionAnswer>
              </AnswerSpecification>
          </Question>
    
    </QuestionForm>
    """
    return questions


def def_answers():
    """
    Answers to the test questions (ground-truth scores). Make sure to update QualificationValueMapping according to the max score.
    """
    answers = """
    <AnswerKey xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd">
      <Question>
        <QuestionIdentifier>Query1</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A1</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A2</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A3</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A4</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
            </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A5</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
      </Question>
    
       <Question>
        <QuestionIdentifier>Query2</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A21</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A22</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A23</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A24</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A25</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
      </Question>
    
       <Question>
        <QuestionIdentifier>Query3</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A31</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A32</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A33</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A34</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A35</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
      </Question>
    
       <Question>
        <QuestionIdentifier>Query4</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A41</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A42</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A43</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A44</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A45</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
      </Question>
     
    
       <Question>
        <QuestionIdentifier>Query7</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A71</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A72</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A73</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A74</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A75</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
      </Question>
    
       <Question>
        <QuestionIdentifier>Query8</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A81</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A82</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A83</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A84</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A85</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
      </Question>
    
         <Question>
        <QuestionIdentifier>Query11</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A111</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A112</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A113</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A114</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A115</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
      </Question>
    
       <Question>
        <QuestionIdentifier>Query12</QuestionIdentifier>
        <AnswerOption>
          <SelectionIdentifier>A121</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A122</SelectionIdentifier>
          <AnswerScore>0</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A123</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
        <AnswerOption>
          <SelectionIdentifier>A124</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
                      </AnswerOption>
              <AnswerOption>
          <SelectionIdentifier>A125</SelectionIdentifier>
          <AnswerScore>1</AnswerScore>
        </AnswerOption>
      </Question>
    
    
      <QualificationValueMapping>
        <PercentageMapping>
          <MaximumSummedScore>8</MaximumSummedScore>
        </PercentageMapping>
      </QualificationValueMapping>
    </AnswerKey>
    """
    return answers


def create_qualifications(client, q_name, questions, answers, existing_qualification=False):
    """
    Creates the qualifications for the HIT we'll create.
    "localRequirements" defined all qualifications where "qual_type_ID" is our tailored made test questions qualification.
    """
    if existing_qualification:
        with open("test_qualification_id.txt", "r") as id_file:
            qual_type_ID = id_file.readlines()[0]
            print("Using existed test qualification with ID:", qual_type_ID)
    else:
        qual_response = client.create_qualification_type(
            Name=q_name,
            Keywords='test, qualification, humor, ig nobel',
            Description='This is a brief scientific humor test',
            QualificationTypeStatus='Active',
            Test=questions,
            AnswerKey=answers,
            TestDurationInSeconds=600)

        qual_type_ID = qual_response['QualificationType']['QualificationTypeId']
        print(qual_type_ID)
        with open("test_qualification_id.txt", "w") as id_file:
            id_file.write(qual_type_ID)

    localRequirements = [
        {'QualificationTypeId': '00000000000000000071',  #location
         'Comparator': 'In',
         'LocaleValues': [{'Country': 'US'}]},
        {'QualificationTypeId': '000000000000000000L0',  #% approved
         'Comparator': 'GreaterThanOrEqualTo',
         'IntegerValues': [97]},
        {'QualificationTypeId': '00000000000000000040',  # num approved
         'Comparator': 'GreaterThan',
         'IntegerValues': [1000]},
        {'QualificationTypeId': qual_type_ID,
         'Comparator': 'GreaterThan',
         'IntegerValues': [87]}
        # ,'RequiredToPreview': False
        # }
    ]
    return localRequirements


#################### HIT creation ####################
def instructions():
    """
    HTML instructions for the HIT
    """
    instructions = """
    <h1>Overview</h1>
    
    <p>Science is important, serious and often boring. We are interested in finding those<strong>&nbsp;rare events in which research is also funny</strong>.</p>
    
    <p>In this job, we provide you with titles of <strong>real&nbsp;</strong><strong>research papers</strong>. Your task is to determine whether they're funny or not. Specifically, to rank two things:
    
    
        <br>(1) How funny the <strong><span style="color: rgb(184, 49, 47);">title</span></strong> is and (2) how funny the<span style="color: rgb(41, 105, 176);">&nbsp;</span><strong><span style="color: rgb(41, 105, 176);">research topic</span></strong> is.</p>
    
    <table style="width: 100%;">
        <tbody>
            <tr>
                <td style="width: 100%; border: 3px solid rgb(147, 101, 184);"><strong>&nbsp; Funny <span style="color: rgb(184, 49, 47);">title</span>&nbsp;</strong>means that the sentence itself is funny, regardless of scientific research (e.g., uses puns,).
                    <br><strong>&nbsp; Funny<span style="color: rgb(41, 105, 176);">&nbsp;research topic</span></strong> means that this is a peculiar thing for scientists to deal with.
                    <br>
                </td>
            </tr>
        </tbody>
    </table>
    
    <p>
        <br>
    </p>
    <hr>
    
    <!--------------------------------------------Steps-------------------------------------------->
    <h1>Steps</h1>
    <h3>
    
    <p><strong>For each title:</strong></p>
        <ol>
            <li><strong>Determine how funny the <span style="color: rgb(184, 49, 47);">title</span> is.</strong></li>
            <li><strong>Determine how funny the&nbsp;</strong><strong><span style="color: rgb(41, 105, 176);">topic</span></strong><strong>&nbsp;is.</strong></li>
        </ol>
    </h3>
    
        <p>On a scale of 1 to 5, where:&nbsp;1 - not funny (or I don't understand), 3 - somewhat funny, 5 - very funny. <br />
        Feel free to look stuff up. If you <strong>completely do not understand</strong> a title, mark it as "not funny" (score=1) — if you don't get it, it definitely does not make you laugh.</p>
    <hr>
    
    <!--------------------------------------------Examples-------------------------------------------->
    <h1>Examples</h1>
    
        <div><strong>There are four different scenarios, as described below.</strong></div>
    
        <ul>
            <li>
                <div><span style="color: rgb(0, 0, 0);"><strong><u>Serious</u></strong></span><span style="color: rgb(0, 0, 0);"><strong><u>&nbsp;<span style="color: rgb(41, 105, 176);"><strong>research topic</strong></span></u><span style="color: rgb(0, 0, 0);"><strong><u>:</u></strong></span></strong>
                    </span>
                </div>
                <ul>
                    <li>
                        <div><span style="color: rgb(0, 0, 0);"><strong>Funny <span style="color: rgb(184, 49, 47);"><strong>title<span style="color: rgb(0, 0, 0);"><strong>:&nbsp;</strong></span></strong>
                            </span>
                            </strong>
                            </span><span style="color: rgb(0, 0, 0);">these papers have funny&nbsp;</span><span style="color: rgb(184, 49, 47);">titles</span><span style="color: rgb(0, 0, 0);">, but the&nbsp;</span><span style="color: rgb(41, 105, 176);">topic</span><span style="color: rgb(0, 0, 0);">&nbsp;does not sound funny (or not clear) — &nbsp;4 on&nbsp;</span><span style="color: rgb(184, 49, 47);">title</span><span style="color: rgb(0, 0, 0);">&nbsp;and 1 on the</span><span style="color: rgb(37, 25, 55);">&nbsp;</span><span style="color: rgb(41, 105, 176);">research topic</span><span style="color: rgb(0, 0, 0);">.&nbsp;</span>
                            <br>
                            <ul>
                                <li>
                                    <div><span style="color: rgb(0, 0, 0);">"<em><strong>Are you certain about SIRT?</strong></em>"&nbsp;</span></div>
                                </li>
                                <li>
                                    <div><span style="color: rgb(0, 0, 0);">"<em><strong>NASH may be trash</strong></em>"<br></span></div>
                                </li>
                                <li>
                                    <div><span style="color: rgb(0, 0, 0);">"<strong><em>Creep in chipboard</em></strong>"</span></div>
                                </li>
                                <li>
                                    <div><span style="color: rgb(0, 0, 0);">"<em><strong>Snus is not Harmless!</strong></em>"</span></div>
                                </li>
                                <li>
                                    <div><span style="color: rgb(0, 0, 0);">"<em><strong>Knowing how we know: evidentiality and cognitive development</strong></em>"</span></div>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <div><span style="color: rgb(0, 0, 0);"><strong>Serious</strong></span><span style="color: rgb(0, 0, 0);"><strong>&nbsp;<span style="color: rgb(184, 49, 47);"><strong>title<span style="color: rgb(0, 0, 0);"><strong>:&nbsp;</strong></span></strong>
                            </span>
                            </strong>
                            </span><span style="color: rgb(0, 0, 0);">the following paper is not funny at all (</span><span style="color: rgb(184, 49, 47);">title</span><span style="color: rgb(0, 0, 0);">&nbsp;and&nbsp;</span><span style="color: rgb(41, 105, 176);">topic</span><span style="color: rgb(0, 0, 0);">) — 1 for both.</span></div>
                        <ul>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>Fringe Waves from a Wedge With One Face Electric and the Other Face Magnetic</strong></em>"&nbsp;</span></div>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
        <div>
        </div>
        <ul>
            <li>
                <div><span style="color: rgb(0, 0, 0);"><strong><u>Funny <span style="color: rgb(41, 105, 176);"><strong>research topic</strong></span></u><span style="color: rgb(0, 0, 0);"><strong><u>:</u></strong></span></strong>
                    </span>
                </div>
                <ul>
                    <li>
                        <div><span style="color: rgb(0, 0, 0);"><strong>Funny <span style="color: rgb(184, 49, 47);"><strong>title<span style="color: rgb(0, 0, 0);"><strong>: &nbsp;</strong></span></strong>
                            </span>
                            </strong>
                            </span><span style="color: rgb(0, 0, 0);">these papers are very funny (</span><span style="color: rgb(184, 49, 47);">title</span><span style="color: rgb(0, 0, 0);">&nbsp;and&nbsp;</span><span style="color: rgb(41, 105, 176);">topic</span><span style="color: rgb(0, 0, 0);">) — 5 for both.</span></div>
    
                        <ul>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);"><em><strong>Will Humans Swim Faster Or Slower in Syrup?</strong></em>"</span></div>
                            </li>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>The Effect of Country Music on Suicide</strong></em>"&nbsp;</span></div>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <div><span style="color: rgb(0, 0, 0);"><strong>Serious</strong></span><span style="color: rgb(0, 0, 0);"><strong>&nbsp;<span style="color: rgb(184, 49, 47);"><strong>title<span style="color: rgb(0, 0, 0);"><strong>: &nbsp;</strong></span></strong>
                            </span>
                            </strong>
                            </span><span style="color: rgb(0, 0, 0);">this scenario is the most elusive. The following papers have a somewhat-serious&nbsp;</span><span style="color: rgb(184, 49, 47);">title&nbsp;</span><span style="color: rgb(0, 0, 0);">for a pretty funny&nbsp;</span><span style="color: rgb(41, 105, 176);">research topic</span><span style="color: rgb(0, 0, 0);">&nbsp;— 2 on&nbsp;</span><span style="color: rgb(184, 49, 47);">title</span><span style="color: rgb(0, 0, 0);">&nbsp;and 5 on the&nbsp;</span><span style="color: rgb(41, 105, 176);">topic</span><span style="color: rgb(0, 0, 0);">.</span></div>
                        <ul>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>Playing 'Tetris' reduces the strength, frequency and vividness of naturally occurring cravings</strong></em>"</span></div>
                            </li>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>Optimizing the Sensory Characteristics and Acceptance of Canned Cat Food: Use of a Human Taste Panel</strong></em>"</span></div>
                            </li>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>The Effect of Wok Size and Handle Angle on the Maximum Acceptable Weights of Wok Flipping by Male Cooks</strong></em>"</span></div>
                            </li>
                            <li>
                                <div><span style="color: rgb(0, 0, 0);">"<em><strong>How the Brain Responds to the Destruction of Money</strong></em>"&nbsp;</span></div>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    
    """
    return instructions


def HIT_creation(client, HIT_name, localRequirements, df_titles, verbos=True, existing_qualification=False):
    """
    Creates the HIT with the qualifications defined according to "local_requirements".
    Create a file with all HITs' IDs (hitIdFile) and a file with titles' IDs AND HITs' IDs.
    """
    if existing_qualification:
        hitIdFile = open("hit_ids.txt", "a")
        hitId2titleID = open("hit_id2title_id.txt", "a")
        pickle_name = "HIT_ids_title_ids"+str(random.randint(0, 10))+".pickle" # To not run over the existing pickle file
    else:
        hitIdFile = open("hit_ids.txt", "w")
        hitId2titleID = open("hit_id2title_id.txt", "w")
        pickle_name = "HIT_ids_title_ids.pickle"
    id_dict = dict()

    for i, row in tqdm(df_titles.iterrows()):
        title_old = row["title"].strip()
        title = ''.join([i if ord(i) < 128 else '' for i in title_old])
        if title_old != title:
            print(i, title)
        if title[-1] not in {".", "!", "?"}:
            title += "."
        question = open('questions.xml', 'r').read()
        question = question.replace("${title}", title)
        new_hit = client.create_hit(
            Title = HIT_name,
            Description = "In this job, we provide you with titles of real research papers. Your task is to determine whether they're funny or not.",
            Keywords = 'humor, science',
            Reward = '0.04',
            MaxAssignments = 3,
            LifetimeInSeconds = 172800,
            AssignmentDurationInSeconds = 600,
            AutoApprovalDelayInSeconds = 14400,
            Question = question,
            QualificationRequirements = localRequirements  # qualifications
        )
        hitIdFile.write(new_hit['HIT']['HITId'] +'\n')
        id_dict[new_hit['HIT']['HITId']] = row["id"]
        hitId2titleID.write(row["id"] + ", " + new_hit['HIT']['HITId'] + '\n')
        
    pickle.dump(id_dict, open(pickle_name, "wb"))
    hitIdFile.close()
    hitId2titleID.close()
    if verbos:
        print("Total number of HITs created in this run is", i+1)
        print("# of lines in hit_ids.txt is", sum(1 for line in open("hit_ids.txt", "r")))
        print("# of lines in hit_id2title_id.txt is", sum(1 for line in open("hit_id2title_id.txt", "r")))

    print("A new HIT has been created. You can preview it here:")
    print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
    print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")
    # Remember to modify the URL above when you're publishing
    # HITs to the live marketplace.
    # Use: https://worker.mturk.com/mturk/preview?groupId=


def responses(client):
    """
    Collects users' responses using HITs' IDs saved in a file using HIT_creation function.
    """
    assignmentsLists=[]
    ID_responses = dict()
    with open("hit_ids.txt", "r") as fp:
        line = fp.readline()
        while line:
            assignmentsList = client.list_assignments_for_hit(
                HITId=line.strip(),
                AssignmentStatuses=['Submitted', 'Approved'],
                MaxResults=10
            )
            print(line)
            print(assignmentsList['Assignments'])
            assignmentsLists.append(assignmentsList['Assignments'])
            line = fp.readline()

    with open('fullbatch3.pickle', 'wb') as handle:
        pickle.dump(assignmentsLists, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('fullbatchIDs.pickle', 'wb') as handle:
        pickle.dump(ID_responses, handle, protocol=pickle.HIGHEST_PROTOCOL)


def main():
    # add_HIT_to_qualification and create_HIT_with_qualifications cannot are disjoint
    add_HIT_to_qualification = True  # True when we want to new HIT to existing qualifications (ID taken from file)
    create_HIT_with_qualifications = not add_HIT_to_qualification  # True when we want to create new HIT with qualifications
    collect_responses = False  # True when we want to collect responses for the HIT (ID taken from file)
    verbos = True  # whether to print account balance and sizes of the files created with the HITs ids

    df_titles = pd.read_csv("mturk_data.csv")

    # Establishing mturk connection
    client = boto3.client('mturk',
                          endpoint_url=endpoint_url,
                          region_name=region_name,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    if verbos:
        print(client.get_account_balance())  # [$10,000.00]

    if create_HIT_with_qualifications or add_HIT_to_qualification:
        q_name = "Can Science Be Funny??"
        HIT_name = "Can Science Be Funny??
        questions = def_questions()
        answers = def_answers()

        localRequirements = create_qualifications(client, q_name, questions, answers,
                                                      existing_qualification=add_HIT_to_qualification)
        HIT_creation(client, HIT_name, localRequirements, df_titles, verbos=verbos,
                                                       existing_qualification=add_HIT_to_qualification)

    if collect_responses:
        responses(client)


if __name__ == "__main__":
    main()



