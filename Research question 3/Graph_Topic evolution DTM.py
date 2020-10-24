# Import essential libraries
import pandas as pd
import ast
import matplotlib.pyplot as plt

# Open the file, read the result of DTM (topic evolution)
with open(r"\DTM_6timeslices.csv", 'r', encoding='utf-8') as file:
    df = pd.read_csv(file)

# Create a function to convert the topic string (literally displayed as dict) to dictionary
def convert_toDict(topic):
    topic_i=[]
    for line in topic:
        sub={}
        line = ast.literal_eval (line)
        for tup in line:
            sub[tup[0]]=tup[1]
        topic_i.append(sub)
    return topic_i

# Create a function to get terms and their probabilities from all topics
def get_term_prob (term, topic):
    term_list=[]
    for item in topic:
        if term in item.keys():
            for k, v in item.items():
                if k ==term:
                    term_list.append(v)
        else:
            term_list.append(0)
    return term_list


# Extract terms and term probabilities from the topics to save separately
# Topic 0
topic_0 = convert_toDict(df["Topic 0"])
pollution = get_term_prob("pollution",topic_0)
environment = get_term_prob("environment",topic_0)
change = get_term_prob("change",topic_0)
temperature = get_term_prob("temperature",topic_0)
increase = get_term_prob("increase",topic_0)
impact = get_term_prob("impact",topic_0)
human = get_term_prob("human",topic_0)

# Topic 1
topic_1 = convert_toDict(df["Topic 1"])
diabet = get_term_prob("diabet",topic_1)
lung = get_term_prob("lung",topic_1)
pulmonary = get_term_prob("pulmonary",topic_1)
acute = get_term_prob("acute",topic_1)
severe_2 = get_term_prob("severe",topic_1)
cytokin = get_term_prob("cytokin",topic_1)
injury = get_term_prob("injury",topic_1)

# Topic 2
topic_2 = convert_toDict(df["Topic 2"])
mask = get_term_prob("mask",topic_2)
protect = get_term_prob("protect",topic_2)
risk = get_term_prob("risk",topic_2)
infection_3 = get_term_prob("infection",topic_2)
healthcare = get_term_prob("healthcare",topic_2)
surgical = get_term_prob("surgical",topic_2)
measure = get_term_prob("measure",topic_2)

# Topic 3
topic_3 = convert_toDict(df["Topic 3"])
test = get_term_prob("test",topic_3)
detect = get_term_prob("detect",topic_3)
sample = get_term_prob("sample",topic_3)
infection_4 = get_term_prob("infection",topic_3)
result = get_term_prob("result",topic_3)
viral = get_term_prob("viral",topic_3)
method = get_term_prob("method",topic_3)

# Topic 5
topic_5 = convert_toDict(df["Topic 5"])
health = get_term_prob("health",topic_5)
community = get_term_prob("community",topic_5)
system = get_term_prob("system",topic_5)
medical = get_term_prob("medical",topic_5)
service = get_term_prob("service",topic_5)
provide = get_term_prob("provide",topic_5)
care = get_term_prob("care",topic_5)

# Topic 6
topic_6 = convert_toDict(df["Topic 6"])
social = get_term_prob("social",topic_6)
study = get_term_prob("study",topic_6)
anxiety = get_term_prob("anxiety",topic_6)
survey = get_term_prob("survey",topic_6)
mental = get_term_prob("mental",topic_6)
psychology = get_term_prob("psychology",topic_6)
participant = get_term_prob("participant",topic_6)

# Topic 7
topic_7 = convert_toDict(df["Topic 7"])
cell = get_term_prob("cell",topic_7)
sarscov2 = get_term_prob("sarscov2",topic_7)
protein = get_term_prob("protein",topic_7)
virus = get_term_prob("virus",topic_7)
vaccine = get_term_prob("vaccine",topic_7)
immune = get_term_prob("immune",topic_7)
ace2 = get_term_prob("ace2",topic_7)

# Topic 10
topic_10 = convert_toDict(df["Topic 10"])
drug = get_term_prob("drug",topic_10)
treatment = get_term_prob("treatment",topic_10)
cancer = get_term_prob("cancer",topic_10)
trial = get_term_prob("trial",topic_10)
antivirus = get_term_prob("antivirus",topic_10)
therapy = get_term_prob("therapy",topic_10)
combine = get_term_prob("combine",topic_10)

# Topic 11
topic_11 = convert_toDict(df["Topic 11"])
patient = get_term_prob("patient",topic_11)
clinical = get_term_prob("clinical",topic_11)
symptom = get_term_prob("symptom",topic_11)
severe_12 = get_term_prob("severe",topic_11)
disease = get_term_prob("disease",topic_11)
pneumonia = get_term_prob("pneumonia",topic_11)
chest = get_term_prob("chest",topic_11)


# Plot the topic evolution graph
# Create subplots
fig, ((plt1, plt2, plt3), (plt4, plt6, plt7), (plt8, plt11, plt12)) = plt.subplots(3, 3, figsize=(15, 13), sharex=True)

# Create a function to plot lines within subplots
def plot_line (t1,t2,t3,t4,t5,t6,t7, plt, str_label):
    x=['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6']
    plt.plot(x, t1, label=convert_VarTostr(t1))
    plt.plot(x, t2, label=convert_VarTostr(t2))
    plt.plot(x, t3, label=convert_VarTostr(t3))
    plt.plot(x, t4, label=convert_VarTostr(t4))
    plt.plot(x, t5, label=convert_VarTostr(t5))
    plt.plot(x, t6, label=convert_VarTostr(t6))
    plt.plot(x, t7, label=convert_VarTostr(t7))
    plt.set_title(str_label)
    plt.legend(loc='lower left', bbox_to_anchor=(0.01, 0.005), fontsize=8)
    return plt

def convert_VarTostr(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    f= [var_name for var_name, var_val in callers_local_vars if var_val is var]
    return f[0]

# Plot subgraphs by using created functions
plt1=plot_line(pollution,environment,change, temperature,increase, impact,human,plt1, 'Effects of the environment on Covid-19')
plt2=plot_line(diabet,lung,pulmonary,acute, severe_2,cytokin, injury, plt2, 'Covid-19 with patients having severe diseases')
plt3=plot_line(mask,protect,risk,infection_3, healthcare,surgical, measure,plt3, 'Preventing  infection by wearing masks')
plt4= plot_line(test, detect, sample, infection_4,result, viral, method,plt4, 'Covid-19 testing methods')
plt6=plot_line(health,community,system,medical, service, provide, care, plt6, 'Challenges of the public healthcare system' )
plt7=plot_line(social, study,anxiety, survey,mental, psychology, participant,plt7, 'Studies on psychological effects of Covid-19' )
plt8=plot_line(cell,sarscov2,protein, virus, vaccine, immune, ace2, plt8,'Covid-19 vaccine')
plt11=plot_line(drug,treatment,cancer, trial, antivirus, therapy, combine,plt11, 'Covid-19 treatments')
plt12=plot_line(patient, clinical,symptom,severe_12,disease, pneumonia, chest, plt12, 'Symptoms of Covid-19')

# Save the graph
fig.savefig("\DTM_timeslices.png")
