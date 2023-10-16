<template>
  <q-page class="row items-center justify-evenly">
    {{  api_data  }}
    <example-component
      title="Example component"
      active
      :todos="todos"
      :meta="meta"
    ></example-component>
  </q-page>
</template>

<script setup lang="ts">
import { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/ExampleComponent.vue';
import { inject, onBeforeMount, ref } from 'vue';
import { AxiosInstance } from 'axios';

const $api = inject('$api') as AxiosInstance;

var api_data = ref<object>({'msg': 'no data'})

onBeforeMount(async () => {
  const response = await $api.get('/hello_world')
  api_data.value = response.data
})

const todos = ref<Todo[]>([
  {
    id: 1,
    content: 'ct1'
  },
  {
    id: 2,
    content: 'ct2'
  },
  {
    id: 3,
    content: 'ct3'
  },
  {
    id: 4,
    content: 'ct4'
  },
  {
    id: 5,
    content: 'ct5'
  }
]);
const meta = ref<Meta>({
  totalCount: 1200
});

</script>
