<template>
  <q-page class="row items-center justify-evenly">
    <chat-box />
  </q-page>
</template>

<script setup lang="ts">
import ChatBox from 'src/components/ChatBox.vue';
import { inject, onBeforeMount, ref } from 'vue';
import { AxiosInstance } from 'axios';

const $api = inject('$api') as AxiosInstance;

var api_data = ref<object>({'msg': 'no data'})

onBeforeMount(async () => {
  const response = await $api.get('/hello_world')
  api_data.value = response.data
})
</script>
