-- Schema: public
CREATE SCHEMA public;

-- Table: public.source
CREATE TABLE public.source
(
    source_id serial NOT NULL,
    name character varying(255) NOT NULL,
    CONSTRAINT source_pkey PRIMARY KEY (source_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Table: public.author
CREATE TABLE public.author
(
    author_id serial NOT NULL,
    name character varying(255) NOT NULL,
    CONSTRAINT author_pkey PRIMARY KEY (author_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;


-- Table: public.article
CREATE TABLE public.article
(
    article_id serial NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    publication_date date NOT NULL,
    url character varying(255) NOT NULL,
    author_id character varying(255),
    source_id integer,
    category character varying(255) NOT NULL,
    CONSTRAINT article_pkey PRIMARY KEY (article_id),
    CONSTRAINT article_author_id_fkey FOREIGN KEY (author_id)
        REFERENCES public.author (author_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT article_source_id_fkey FOREIGN KEY (source_id)
        REFERENCES public.source (source_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Grants
GRANT ALL ON TABLE public.article TO postgres;
GRANT ALL ON TABLE public.source TO postgres;
GRANT ALL ON TABLE public.author TO postgres;