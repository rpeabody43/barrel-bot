# freezes dependencies with proper encoding so the SAM deployment doesn't throw a fit
pip freeze | Out-File -Encoding UTF8 lambda/requirements.txt