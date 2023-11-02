<template>
    <q-table
        title="Knowledge Files"
        :columns="columns"
        :rows="file_uploads"
        row-key="name"
    />
</template>

<script setup lang="ts">
import { inject, onBeforeMount, ref } from 'vue';
import { AxiosInstance } from 'axios';

const columns: {
    name: string;
    label: string;
    field: string | ((row: object) => string | number);
    required?: boolean; align?: 'center' | 'left' | 'right';
    sortable?: boolean;
}[] = [
    {
        name: 'uploaded',
        align: 'center',
        label: 'Uploaded',
        field: 'uploaded_at',
        sortable: true
    },
    {
        name: 'name',
        required: true,
        label: 'Name',
        align: 'left',
        field: 'raw_filename',
        sortable: true
    },
    {
        name: 'size_bytes',
        align: 'right',
        label: 'Size (bytes)',
        field: 'size_bytes',
        sortable: true
    },
    {
        name: 'num_chunks',
        align: 'right',
        label: 'Num Chunks',
        field: 'num_chunks',
        sortable: true
    },
    {
        name: 'status',
        align: 'center',
        label: 'Status',
        field: 'status',
        sortable: true
    }
];

const $api = inject('$api') as AxiosInstance;

const file_uploads = ref<object[]>([]);

async function getFileUploads() {
    const response = await $api.get('/file_uploads')
    file_uploads.value = response.data.file_uploads
}

onBeforeMount(getFileUploads)

defineExpose({
    getFileUploads
})

</script>
