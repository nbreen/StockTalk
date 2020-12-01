import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { CrudService } from './crud.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// import for UI
import { MyMaterialModule } from './material.module';
import { AlltopicsComponent } from './alltopics/alltopics.component';
import { TrendingtopicsComponent } from './trendingtopics/trendingtopics.component';
import { TopicComponent } from './alltopics/topic/topic.component';
import { PostComponent } from './alltopics/topic/post/post.component';
import { CommentComponent } from './alltopics/topic/post/comment/comment.component';
import { ProfileComponent } from './profile/profile.component';
import { Globals } from './Globals';
import { DeleteUserComponent } from './delete-user/delete-user.component';
import { ProfileSettingsComponent } from './profile-settings/profile-settings.component';
import { MakePostComponent } from './make-post/make-post.component';
import { FollowersComponent } from './followers/followers.component';
import { ViewSavedPostsComponent } from './view-saved-posts/view-saved-posts.component';
import { ViewSinglePostComponent } from './view-single-post/view-single-post.component';
import { SuggestionsComponent } from './suggestions/suggestions.component';
import { VerifyComponent } from './verify/verify.component';
import { MakeCommentComponent } from './make-comment/make-comment.component';
import { HomepageComponent } from './homepage/homepage.component';;
import { HomePageComponent } from './home-page/home-page.component';;

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    AlltopicsComponent,
    TrendingtopicsComponent,
    TopicComponent,
    PostComponent,
    CommentComponent,
    ProfileComponent,
    DeleteUserComponent,
    ProfileSettingsComponent,
    MakePostComponent,
    FollowersComponent,
    ViewSavedPostsComponent,
    ViewSinglePostComponent,
    SuggestionsComponent,
    VerifyComponent,
    MakeCommentComponent,
    HomepageComponent,
    HomePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MyMaterialModule
  ],
  providers: [CrudService, Globals],
  bootstrap: [AppComponent]
})
export class AppModule { }
