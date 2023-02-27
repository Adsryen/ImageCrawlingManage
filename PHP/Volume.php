<?php
    $link=mysqli_connect("122.9.153.176","xiuren","6sfitTyZJdFFzYYP");      //链接数据库
    mysqli_select_db($link,"xiuren");                       
    mysqli_query($link,"set names 'utf8'");                   //设置字符集
    if(isset($_GET['VolumeUrl'])){
        $VolumeUrl = $_GET['VolumeUrl'];
    }
    else{
        $VolumeUrl = "XiuRen_VolumeUrl";
    }

    if(isset($_GET['VolumeID'])){
    $VolumeID = $_GET['VolumeID'];
    }
    else{
        $VolumeID = "";
    }

    $str = "select * from ".$VolumeUrl;         //数据库查询语句
    $str.= " WHERE VolumeID=".$VolumeID;
    $str.= " ORDER BY ImgsID ASC";
    $result = mysqli_query($link,$str);           
    // $row = mysqli_fetch_assoc($result);           //将结果以数组的形式反馈给result1
    // echo mysqli_num_rows($result);

?>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="https://www.prlrr.com/wallpaper-API/php-api/Avatar.php">
    <link rel="stylesheet" href="./reset.min.css">
    <link rel='stylesheet' href='./googleapis.css'>
    <link rel="stylesheet" href="./style.css">
    <link rel="stylesheet" href="./Volume.css">
</head>
<body>
    <h1 class="title">Some nice pamphlets</h1>
    <?php
        if (mysqli_num_rows($result)>0){
            $row1 = mysqli_fetch_assoc($result);
            echo "<p class='title' >{$row1['Volume2Name']}</p>";
            echo "
                    <div id='gallery'>
                        <a title=''><img src='{$row1['ImgsUrl']}' width='950px' alt='{$row1['ImgsID']}' /></a>
                    </div> ";
            while ($row = mysqli_fetch_assoc($result)){
                $img_htmls = "
                    <div id='gallery'>
                        <a title=''><img src='{$row['ImgsUrl']}' width='950px' alt='{$row['ImgsID']}' /></a>
                    </div> 
                ";
                echo $img_htmls;
            
            } 
            echo "<p class='foot'>End</p>";
        }
        else{
            echo "<p class='foot'>该图册暂时无法查看，请稍后再试！</p>";
        }
           
        
    ?>
    
</body>
</html>
