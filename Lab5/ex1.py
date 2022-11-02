from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

card_game = BayesianNetwork(
    [
        ("c1", "c2"),
        ("c1", "r1"),
        ("c2", "r2"),
        ("r1", "r2"),
        ("r2", "r3"),
    ]
)

from pgmpy.factors.discrete import TabularCPD

cpd_c1 = TabularCPD(
    variable="c1",
    variable_card=5,
    values=[[0.2], [0.2],[0.2],[0.2],[0.2]]
)

cpd_c2 = TabularCPD(
    cpd_alarm=TabularCPD(
    variable="c2",
    variable_card=5,
    values=[[0,0.25,0.25,0.25,0.25],
            [0.25,0,0.25,0.25,0.25],
            [0.25,0.25,0,0.25,0.25],
            [0.25,0.25,0.25,0,0.25],
            [0.25,0.25,0.25,0.25,0]],
    evidence=["c1"],
    evidence_card=[5,5],
    )
)

cpd_r1 = TabularCPD(
    cpd_alarm=TabularCPD(
    variable="r1",
    variable_card=2,
    values=[
        [1,0.85,0.5,0.3,0],
        [0,0.15,0.5,0.7,1],
        ],
    evidence=["c1"],
    evidence_card=[5],
    )
)

cpd_r2 = TabularCPD(
    cpd_alarm=TabularCPD(
    variable="r2",
    variable_card=3,
    values=[
        [1,0.8,0.45,0,0,1,1,0.5,0,0],
        [0,0,0,0,0,0,0,0,0,0.3,0.6],
        [0,0.2,0.55,1,1,0,0,0.5,0.7,0.4],
    ],
    evidence=["c1","r1"],
    evidence_card=[10,3],
    )
)

cpd_r3 = TabularCPD(
    cpd_alarm=TabularCPD(
    variable="r3",
    variable_card=3,
    values=[
        [1,0.8,0.45,0,0,1,1,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0.3,0.6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0.2,0.55,1,1,0,0,0.5,0.7,0.4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ],
    evidence=["r2","r1", "c1"],
    evidence_card=[10,3],
    )
)

model.add_cpds(cpd_c1, cpd_c2, cpd_r1,cpd_r2, cpd_r3)
infer = VariableElimination(model)
posterior_p1 = infer.query(["r1"], evidence={"c1": 2})
posterior_p = infer.query(["r2"], evidence={"c2":3,"r1":1})
print(posterior_p,posterior_p1)
