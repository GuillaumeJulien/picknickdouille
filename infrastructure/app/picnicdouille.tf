terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">= 0.13"
}

provider "scaleway" {
  zone   = "fr-par-1"
  region = "fr-par"
}

resource scaleway_container_namespace main {
    name = "picnicdouille-app"
    description = "application de l'équipe rose pour tirer au sort"
}

resource scaleway_container main {
    name = "picnicdouille-container"
    description = "environment variables test"
    namespace_id = scaleway_container_namespace.main.id
    registry_image = "${scaleway_container_namespace.main.registry_endpoint}/alpine:test"
    port = 5000
    cpu_limit = 70
    memory_limit = 128
    min_scale = 1
    max_scale = 2
    privacy = "private"
    protocol = "http1"
    deploy = true
}

