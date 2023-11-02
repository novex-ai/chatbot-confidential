<template>
    <q-page
        class="data-page column q-gutter-md q-ma-none"
        style="width: 100%;"
    >
        <q-uploader
            :url="uploaderUrl"
            label="Upload Knowledge Files"
            color="primary"
            multiple
            style="width: 100%;"
            @finish="onFileUploadFinish"
        />
        <UploadedDataTable ref="uploadedDataTable" />
    </q-page>
</template>

<script setup lang="ts">
import {ref} from 'vue';
import UploadedDataTable from 'src/components/UploadedDataTable.vue';

const uploaderUrl: string = import.meta.env.VITE_API_BASE_URL + '/upload';

const uploadedDataTable = ref<typeof UploadedDataTable | null>(null)

async function onFileUploadFinish() {
    await uploadedDataTable.value?.getFileUploads()
}

</script>

<style lang="scss">
.data-page {
    width: 100%;
}
</style>