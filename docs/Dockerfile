FROM ruby:2.7.2-alpine3.12

RUN apk add --no-cache g++ make zlib-dev

WORKDIR /website/ruby
RUN addgroup --system jekyll && adduser --home /website/ruby/jekyll_home --system jekyll -G jekyll
RUN chown -R jekyll:jekyll /website/ruby
USER jekyll

RUN \
    gem install bundler -v 2.2 && \
    bundle config set deployment test && \
    bundle config set path /website/ruby/gems

COPY ./Gemfile .
COPY ./Gemfile.lock .
RUN bundle install

COPY --chown=jekyll:jekyll . /website/ruby/docs

EXPOSE 4000
WORKDIR /website/ruby/docs
CMD bundle exec jekyll serve -H 0.0.0.0 -P 4000