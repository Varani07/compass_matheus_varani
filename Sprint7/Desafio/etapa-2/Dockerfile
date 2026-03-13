FROM public.ecr.aws/sam/build-python3.11

COPY create_layer . 

RUN yum update -y

RUN yum install -y \
python3-pip \
zip

RUN yum -y clean all
