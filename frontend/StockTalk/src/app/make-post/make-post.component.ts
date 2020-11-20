
import { Component, Input, OnInit, HostListener } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CrudService } from '../crud.service'; 
import { Globals } from '../Globals';
import { Profile } from '../shared/profile.model';
import { User } from '../shared/user.model';
import { Post } from '../shared/post.model';
import { Router } from '@angular/router';
import { Topic } from '../Interfaces';
import { NgForm, FormGroup, FormBuilder } from '@angular/forms';
import {DatePipe} from '@angular/common';

@Component({
  selector: 'app-make-post',
  templateUrl: './make-post.component.html',
  styleUrls: ['./make-post.component.scss']
})
export class MakePostComponent implements OnInit {

  stateForm: FormGroup;

  showDropDown = false;

  pic_upload = false;

  postPhotoPath: string;

  /*topics: Array<Topic>;*/
  topics = ['suggest topic1 placeholder', 'suggest topic2 placeholder', 'suggest topic3 placeholder']
  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private backend : CrudService,
    public globals: Globals,
    private router: Router
  ) {

    this.initForm()
    /*
    this.backend.getAll<Topic>("/suggestTopics/0").subscribe(data => {
      console.log(data);
      this.topics = data;
    })*/
  }

  initForm(): FormGroup {
    return this.stateForm = this.fb.group({
      search:[null]
    })
  }

  profile: Profile;
  user: User;

  @Input() new_post: Post = {
    Username: "",
    TopicName: "",
    PostType: 0,
    Post: "",
    PostDate: "placeholder",
    Downvotes: 0,
    Upvotes: 0,
    Anonymous: 0,
    PostImage: "placeholder"
  }

  @HostListener('document:keydown', ['$event'])
  handleKeyboardEvent(event: KeyboardEvent) {
      console.log(event)
    
  }

  resetPost() {
    this.new_post.TopicName = "";
    this.new_post.PostImage = "placeholder";
    this.pic_upload = false;
  }

  submitPost() {

    this.new_post.PostDate = new Date().toLocaleString();
  

    if (this.new_post.TopicName == "") {
      this.new_post.TopicName = "no_topic";
    }

    if (this.new_post.Post == "" ) {
      this.new_post.Post = "no_post";
    }

    if (this.pic_upload) {
      this.new_post.PostImage = this.postPhotoPath;
    }

    this.backend.addPost(this.new_post).subscribe(res => {
      if (res.toString() != "Post added successfully") {
        alert("Something went wrong");
        this.resetPost();
      }
      this.directProfile();
      console.log("post submitted")
    });


  }

  directProfile() {
    this.router.navigate(["/profile/" + this.globals.currentUsername]);
  }

  ngOnInit(): void {
    var url_username = this.route.snapshot.params["User"];

    if (this.globals.currentUsername != url_username) {
      this.router.navigate(["/"]);
    } 

    this.backend.getProfile(this.globals.currentUsername).subscribe(res => {
      var profile_data = JSON.stringify(res);
      profile_data = profile_data.substring(1, profile_data.length-1);
      this.profile = JSON.parse(profile_data);
    });

    this.backend.getUser(this.globals.currentUsername).subscribe(res => {
      var user_data = JSON.stringify(res);
      user_data = user_data.substring(1, user_data.length-1);
      this.user = JSON.parse(user_data);
      this.new_post.Username = this.user.Username;
    });

  }

  toggleDropDown() {
    this.showDropDown = !this.showDropDown;
  }

  selectValue(value) {
    this.stateForm.patchValue({ "search": value});
    this.showDropDown = false;
  }

  getSearchValue() {
    return this.stateForm.value.search;
  }

  uploadPostPic(event){
    var file=event.target.files[0];
    const formData:FormData=new FormData();
    formData.append('uploadedFile',file,file.name);
    this.new_post.PostImage = file.name;
    this.pic_upload = true;

    this.backend.uploadPostPic(formData).subscribe((data:any)=>{
      var photoFileName=data.toString();
      this.postPhotoPath=this.backend.PhotoUrl + photoFileName;
    })
  }

}
