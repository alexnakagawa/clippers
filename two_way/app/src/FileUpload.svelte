<script>
    formidable = require('formidable');
</script>

<form id='jsonupload' enctype='multipart/form-data' method='post' action=''>
    <input type='file' name='fileupload' id='fileupload' accept='.json'>
    <label for='fileupload'> Select a file to upload</label>
    <input type='submit' on:click={uploadFile}>
</form>

<script>
</script>