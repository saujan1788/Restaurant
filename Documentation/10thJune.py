def issues:
    I had an issue on  connecting my prometheus and Grafana service together, Issue was in the service file of the prometheus , Labels were wrong. 


def solution:
    Had to edit the svc file to use the right labels, Since I am using nodeport service, I could connect to promotheus via any node ip in the cluster. Created a dashboard with 4 panels. PromQL queries generated by GPT used. 


