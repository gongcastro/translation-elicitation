pdf:
	quarto render 

docx:
	quarto render --profile docx

render:
	quarto render --profile docx,pdf

docker-build: Dockerfile .dockerignore
	@echo "Building Docker image..."
	@docker build -t translation-elicitation .
	@echo "Pushing image to Dockerhub"
	@docker tag translation-elicitation gongcastro/translation-elicitation:latest
	@docker push gongcastro/translation-elicitation:latest

docker-run:
	@echo "Running Docker container at http://localhost:8787"
	@docker run --rm -ti \
		-e ROOT=true \
		-e PASSWORD=rstudio \
 		-p 8787:8787 \
		--name rstudio gongcastro/translation-elicitation:latest
	