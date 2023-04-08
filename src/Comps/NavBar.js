//<Homepage  />, <AboutUs />, <Activities/>, <AccountPage/>, resurse


const NavBar = ({setContor}) => {
    return ( 
        <div className="navbar">

<p onClick={()=>{setContor(0)}} class="logo">Logo</p>

<div class="infos-container">
    <div onClick={()=>{setContor(2)}} class="info">Activities</div>
    <div onClick={()=>{setContor(4)}} class="info">Resources</div>
    <div onClick={()=>{setContor(1)}} class="info">About Us</div>
</div>

<div onClick={()=>{setContor(3)}} class="user-container">
    <div class="user-info">Username</div>
    <div class="user-info">PFP</div>
</div>

        </div>
     );
}
 
export default NavBar;
<div>

         

</div>