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
import { TopicComponent } from './alltopics/topic/topic.component';
import { PostComponent } from './alltopics/topic/post/post.component';
import { CommentComponent } from './alltopics/topic/post/comment/comment.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    AlltopicsComponent,
    TopicComponent,
    PostComponent,
    CommentComponent
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
  providers: [CrudService],
  bootstrap: [AppComponent]
})
export class AppModule { }
