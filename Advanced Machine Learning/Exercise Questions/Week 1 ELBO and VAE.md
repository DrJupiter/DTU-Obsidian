
## WANB Report

https://api.wandb.ai/links/ai-dtu/fds3crlj


## Programming 1

### 1
![[Pasted image 20240208093747.png]]

The reparametrisation trick is handled by using `rsample` on the distribution returned by the forward network/encoder.


### 2
![[Pasted image 20240208093924.png]]

They have the `batchsize` as shape, probably because of the `td.Independet`, which turns batches into events.

The `batchsize` was `128` in this case:


### 3
![[Pasted image 20240208094749.png]]

 `td.Independet` turns batches into events.
![[Pasted image 20240208094850.png]]

### 4

![[Pasted image 20240208094947.png]]

To extract a mean and covariance.

## Programming 2


![[Pasted image 20240208095041.png]]

### 1

```python
def evaluate(model, data_loader, device):

"""

Evaluate a VAE model.

  

Parameters:

model: [VAE]

The VAE model to evaluate.

data_loader: [torch.utils.data.DataLoader]

The data loader to use for evaluation.

device: [torch.device]

The device to use for evaluation.

"""

	model.eval()

	total_loss = 0

	with torch.no_grad():

		for x in data_loader:

		x = x[0].to(device)

		loss = model(x)

		total_loss += loss.item()

	average_loss = total_loss/len(data_loader)

	wandb.log({"validation-loss": average_loss})

	return average_loss
```
![[Pasted image 20240208120053.png]]

https://wandb.ai/ai-dtu/Advanced%20Machine%20Learning%20Spring%202024/runs/lcfp3sbf?workspace=user-klausjupiter


### 2

![[Pasted image 20240208100218.png]]

![[Pasted image 20240208110447.png]]
![[Pasted image 20240208110500.png]]

![[Pasted image 20240208110522.png]]

This we just have to plot the `self.encoder(x)`.

![[Pasted image 20240208120147.png]]


![[Pasted image 20240208120202.png]]
https://wandb.ai/ai-dtu/Advanced%20Machine%20Learning%20Spring%202024/runs/meft9vmq?workspace=user-klausjupiter