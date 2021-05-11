# github-metadaten-test

{% for repository in site.github.public_repositories %}{% if repository.archived == false %}

    [{{ repository.name }}]({{ repository.html_url }}) {% endif %}{% endfor %}
