"""Dépendance optionnelle : torch. CPU, données synthétiques, aucun téléchargement de dataset."""

import torch
from torch import nn

torch.manual_seed(7)
x = torch.linspace(0, 1, 40).reshape(-1, 1)
y = 2 * x + 1
model = nn.Sequential(nn.Linear(1, 8), nn.Tanh(), nn.Linear(8, 1))
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)
for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    loss = nn.functional.mse_loss(model(x[:24]), y[:24])
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        model.eval()
        with torch.no_grad():
            print(
                epoch,
                "MSE train",
                loss.item(),
                "MSE validation",
                nn.functional.mse_loss(model(x[24:30]), y[24:30]).item(),
            )
model.eval()
with torch.no_grad():
    print("MAE test :", (model(x[30:]) - y[30:]).abs().mean().item())
