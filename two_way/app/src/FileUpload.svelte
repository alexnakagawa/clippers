<script>
    // import formidable from 'formidable';
    import * as storage from '@google-cloud/storage';

    const bucketName = 'lac_dev_test'
    function handleSubmit() {
        var fileUploadElem = document.getElementById('fileupload');
        // console.log(fileUploadElem.value)
        const client = new storage.Storage();
    }
</script>

<form id='jsonupload' enctype='multipart/form-data' method='post' on:submit|preventDefault={handleSubmit}>
    <input type='file' name='fileupload' id='fileupload' accept='.json'>
    <label for='fileupload'>
        By clicking submit, you will be creating/replacing the json file inside of the <code>lac_dev_test</code> bucket in the Google Cloud Project
    </label>
    <input type='submit'>
</form>

<h3>Hello world!</h3>