FROM ubuntu:22.04

WORKDIR /app/

RUN apt-get update && apt-get install socat -y

COPY ./heap-hop /app/run

RUN groupadd --system ctf && \
	useradd -M -d /app -g ctf player && \
	chmod u+sx /app/run

ARG FLAG
RUN echo "${FLAG}" >> /app/flag.txt

RUN chown player:ctf /app/run

USER player

ENTRYPOINT ["socat", "TCP-LISTEN:3000,reuseaddr,fork", "EXEC:'/app/run',stderr"]
